# -*- coding: utf-8 -*-

"""

NEW Changes
======================
Original 1: https://github.com/fyrestone/pydevd_reload
Original 2: https://github.com/fabioz/PyDev.Debugger/blob/main/_pydevd_bundle/pydevd_reload.py

add api for setting auto reload

======================
Based on the python xreload.

Changes
======================
1. we don't recreate the old namespace from new classes. Rather, we keep the existing namespace,
load a new version of it and update only some of the things we can inplace. That way, we don't break
things such as singletons or end up with a second representation of the same class in memory.
2. If we find it to be a __metaclass__, we try to update it as a regular class.
3. We don't remove old attributes (and leave them lying around even if they're no longer used).
4. Reload hooks were changed
These changes make it more stable, especially in the common case (where in a debug session only the
contents of a function are changed), besides providing flexibility for users that want to extend
on it.
Hooks
======================
Classes/modules can be specially crafted to work with the reload (so that it can, for instance,
update some constant which was changed).
1. To participate in the change of some attribute:
    In a module:
    __xreload_old_new__(namespace, name, old, new)
    in a class:
    @classmethod
    __xreload_old_new__(cls, name, old, new)
    A class or module may include a method called '__xreload_old_new__' which is called when we're
    unable to reload a given attribute.
2. To do something after the whole reload is finished:
    In a module:
    __xreload_after_reload_update__(namespace):
    In a class:
    @classmethod
    __xreload_after_reload_update__(cls):
    A class or module may include a method called '__xreload_after_reload_update__' which is called
    after the reload finishes.
Important: when providing a hook, always use the namespace or cls provided and not anything in the global
namespace, as the global namespace are only temporarily created during the reload and may not reflect the
actual application state (while the cls and namespace passed are).
Current limitations
======================
- Attributes/constants are added, but not changed (so singletons and the application state is not
  broken -- use provided hooks to workaround it).
- Code using metaclasses may not always work.
- Functions and methods using decorators (other than classmethod and staticmethod) are not handled
  correctly.
- Renamings are not handled correctly.
- Dependent modules are not reloaded.
- New __slots__ can't be added to existing classes.
Info
======================
Original: http://svn.python.org/projects/sandbox/trunk/xreload/xreload.py
Note: it seems https://github.com/plone/plone.reload/blob/master/plone/reload/xreload.py enhances it (to check later)
Interesting alternative: https://code.google.com/p/reimport/
Alternative to reload().
This works by executing the module in a scratch namespace, and then patching classes, methods and
functions in place.  This avoids the need to patch instances.  New objects are copied into the
target namespace.
"""

import logging
import types
import traceback
import os
import sys
import time
import inspect

NO_DEBUG = 0
LEVEL1 = 1
LEVEL2 = 2

DEBUG = NO_DEBUG


def write_err(*args):
    new_lst = []
    for a in args:
        new_lst.append(str(a))

    msg = ' '.join(new_lst)
    s = 'code reload: %s\n' % (msg,)
    logging.info(s)


def notify_info0(*args):
    write_err(*args)


def notify_info(*args):
    if DEBUG >= LEVEL1:
        write_err(*args)


def notify_info2(*args):
    if DEBUG >= LEVEL2:
        write_err(*args)


def notify_error(*args):
    write_err(*args)


#=======================================================================================================================
# auto reload api
#=======================================================================================================================
class AutoReloader(object):
    ____instance__ = None

    def __init__(self):
        self._boot_time = 0
        self._module_mtime = {}

    @classmethod
    def get_instance(cls):
        if cls.____instance__ is None:
            cls.____instance__ = cls()
        return cls.____instance__

    def setup(self):
        self._boot_time = time.time()

    def refresh(self):
        reload_start_time = time.time()
        invalid_modules = self._get_invalid_module()
        for module in invalid_modules.values():
            xreload(module)
        if invalid_modules:
            logging.info("reload scripts: {}, time: {}".format(
                invalid_modules.keys(),
                time.time() - reload_start_time))

    def _get_invalid_module(self):
        invalid_modules = {}
        modules = dict(sys.modules)
        for name, module in modules.items():
            if inspect.ismodule(module) and self._is_module_need_reload(module):
                invalid_modules[name] = module
        return invalid_modules

    def _is_module_need_reload(self, module):
        filename = getattr(module, "__file__", None)
        if not filename:
            return False
        if os.path.splitext(filename)[-1] == ".pyc":
            filename = filename[:-1]
        try:
            mtime = os.path.getmtime(filename)
        except:
            return False
        last_mtime = self._module_mtime.get(filename, self._boot_time)
        if mtime <= last_mtime:
            return False
        self._module_mtime[filename] = mtime
        return True

def setup():
    AutoReloader.get_instance().setup()

def refresh():
    AutoReloader.get_instance().refresh()

#=======================================================================================================================
# code_objects_equal
#=======================================================================================================================
def code_objects_monkeypatched(code0, code1):
    """
    If the code name changed, the old code probably be monkey patched,
    but monkey patched code object may not change the code name.
    """
    return getattr(code0, 'co_name') != getattr(code1, 'co_name')

def code_objects_equal(code0, code1):
    for d in dir(code0):
        if d.startswith('_') or 'line' in d or d == 'replace':
            continue
        if getattr(code0, d) != getattr(code1, d):
            return False
    return True


#=======================================================================================================================
# xreload
#=======================================================================================================================
def xreload(mod):
    """Reload a module in place, updating classes, methods and functions.
    mod: a module object
    Returns a boolean indicating whether a change was done.
    """
    r = Reload(mod)
    r.apply()
    found_change = r.found_change
    # r = None
    # pydevd_dont_trace.clear_trace_filter_cache()
    return found_change

# This isn't actually used... Initially I planned to reload variables which are immutable on the
# namespace, but this can destroy places where we're saving state, which may not be what we want,
# so, we're being conservative and giving the user hooks if he wants to do a reload.
#
# immutable_types = [int, str, float, tuple] #That should be common to all Python versions
#
# for name in 'long basestr unicode frozenset'.split():
#     try:
#         immutable_types.append(__builtins__[name])
#     except:
#         pass #Just ignore: not all python versions are created equal.
# immutable_types = tuple(immutable_types)


#=======================================================================================================================
# Reload
#=======================================================================================================================
class Reload:

    def __init__(self, mod, mod_name=None, mod_filename=None):
        self.mod = mod
        if mod_name:
            self.mod_name = mod_name
        else:
            self.mod_name = mod.__name__ if mod is not None else None

        if mod_filename:
            self.mod_filename = mod_filename
        else:
            self.mod_filename = mod.__file__ if mod is not None else None

        self.found_change = False

    def apply(self):
        mod = self.mod
        self._updated_objects = set()
        self._on_finish_callbacks = []
        try:
            # Get the module namespace (dict) early; this is part of the type check
            modns = mod.__dict__

            # Execute the code.  We copy the module dict to a temporary; then
            # clear the module dict; then execute the new code in the module
            # dict; then swap things back and around.  This trick (due to
            # Glyph Lefkowitz) ensures that the (readonly) __globals__
            # attribute of methods and functions is set to the correct dict
            # object.
            new_namespace = modns.copy()
            new_namespace.clear()
            if self.mod_filename:
                new_namespace["__file__"] = self.mod_filename
                try:
                    new_namespace["__builtins__"] = __builtins__
                except NameError:
                    raise  # Ok if not there.

            if self.mod_name:
                new_namespace["__name__"] = self.mod_name
                if new_namespace["__name__"] == '__main__':
                    # We do this because usually the __main__ starts-up the program, guarded by
                    # the if __name__ == '__main__', but we don't want to start the program again
                    # on a reload.
                    new_namespace["__name__"] = '__main_reloaded__'

            # execfile(self.mod_filename, new_namespace, new_namespace)
            notify_error("execfile: {}".format(self.mod_filename))
            if self.mod_filename.endswith(".pyc"):
                mod_filename = self.mod_filename[:-1]
            else:
                mod_filename = self.mod_filename
            if sys.version_info.major == 2:
                execfile(mod_filename, new_namespace, new_namespace)
            else:
                exec(compile(open(mod_filename, "rb").read(), self.mod_filename, "exec"), new_namespace, new_namespace)
            # Now we get to the hard part
            oldnames = set(modns)
            newnames = set(new_namespace)

            # Create new tokens (note: not deleting existing)
            for name in newnames - oldnames:
                notify_info0('Added:', name, 'to namespace')
                self.found_change = True
                modns[name] = new_namespace[name]

            # Update in-place what we can
            for name in oldnames & newnames:
                self._update(modns, name, modns[name], new_namespace[name])

            self._handle_namespace(modns)

            for c in self._on_finish_callbacks:
                c()
            del self._on_finish_callbacks[:]
            self._updated_objects.clear()
        except:
            traceback.print_exc()

    def _handle_namespace(self, namespace, is_class_namespace=False):
        on_finish = None
        if is_class_namespace:
            xreload_after_update = getattr(namespace, '__xreload_after_reload_update__', None)
            if xreload_after_update is not None:
                self.found_change = True
                on_finish = lambda: xreload_after_update()

        elif '__xreload_after_reload_update__' in namespace:
            xreload_after_update = namespace['__xreload_after_reload_update__']
            self.found_change = True
            on_finish = lambda: xreload_after_update(namespace)

        if on_finish is not None:
            # If a client wants to know about it, give him a chance.
            self._on_finish_callbacks.append(on_finish)

    def _update(self, namespace, name, oldobj, newobj, is_class_namespace=False):
        """Update oldobj, if possible in place, with newobj.
        If oldobj is immutable, this simply returns newobj.
        Args:
          oldobj: the object to be updated
          newobj: the object used as the source for the update
        """
        try:
            notify_info2('Updating: ', oldobj)
            if id(oldobj) in self._updated_objects:
                return
            self._updated_objects.add(id(oldobj))
            if oldobj is newobj:
                # Probably something imported
                return

            if type(oldobj) is not type(newobj):
                # Cop-out: if the type changed, give up
                if name not in ('__builtins__',):
                    notify_error('Type of: %s (old: %s != new: %s) changed... Skipping.' % (name, type(oldobj), type(newobj)))
                return

            if isinstance(newobj, types.FunctionType):
                self._update_function(oldobj, newobj)
                return

            if isinstance(newobj, types.MethodType):
                self._update_method(oldobj, newobj)
                return

            if isinstance(newobj, classmethod):
                self._update_classmethod(oldobj, newobj)
                return

            if isinstance(newobj, staticmethod):
                self._update_staticmethod(oldobj, newobj)
                return

            if hasattr(types, 'ClassType'):
                classtype = (types.ClassType, type)  # object is not instance of types.ClassType.
            else:
                classtype = type

            if isinstance(newobj, classtype):
                self._update_class(oldobj, newobj)
                return

            # New: dealing with metaclasses.
            if hasattr(newobj, '__metaclass__') and hasattr(newobj, '__class__') and newobj.__metaclass__ == newobj.__class__:
                self._update_class(oldobj, newobj)
                return

            if hasattr(newobj, '__call__'):
                self._update_callable(oldobj, newobj)

            if namespace is not None:
                # Check for the `__xreload_old_new__` protocol (don't even compare things
                # as even doing a comparison may break things -- see: https://github.com/microsoft/debugpy/issues/615).
                xreload_old_new = None
                if is_class_namespace:
                    xreload_old_new = getattr(namespace, '__xreload_old_new__', None)
                    if xreload_old_new is not None:
                        self.found_change = True
                        xreload_old_new(name, oldobj, newobj)

                elif '__xreload_old_new__' in namespace:
                    xreload_old_new = namespace['__xreload_old_new__']
                    xreload_old_new(namespace, name, oldobj, newobj)
                    self.found_change = True

                # Too much information to the user...
                # else:
                #     notify_info0('%s NOT updated. Create __xreload_old_new__(name, old, new) for custom reload' % (name,))

        except:
            notify_error('Exception found when updating %s. Proceeding for other items.' % (name,))
            traceback.print_exc()

    # All of the following functions have the same signature as _update()

    def _update_function(self, oldfunc, newfunc):
        """Update a function object."""
        oldfunc.__doc__ = newfunc.__doc__
        oldfunc.__dict__.update(newfunc.__dict__)

        try:
            oldfunc.__annotations__ = newfunc.__annotations__
        except AttributeError:
            pass  # No function annotation in Python 2.x

        try:
            newfunc.__code__
            attr_name = '__code__'
        except AttributeError:
            newfunc.func_code
            attr_name = 'func_code'

        old_code = getattr(oldfunc, attr_name)
        new_code = getattr(newfunc, attr_name)

        if code_objects_monkeypatched(old_code, new_code):
            notify_error('Code of: %s monkey patched... Skipping.' % (oldfunc,))
            return oldfunc

        if not code_objects_equal(old_code, new_code):
            notify_info0('Updated function code:', oldfunc)
            setattr(oldfunc, attr_name, new_code)
            self.found_change = True

        try:
            oldfunc.__defaults__ = newfunc.__defaults__
        except AttributeError:
            oldfunc.func_defaults = newfunc.func_defaults

        # Update func_closure:
        # 1, skip if function closure count mismatch,
        # 2, only do update by the same function closure sequence.

        try:
            newfunc.__closure__
            attr_name = '__closure__'
        except AttributeError:
            newfunc.func_closure
            attr_name = 'func_closure'

        old_closure = getattr(oldfunc, attr_name) or []
        new_closure = getattr(newfunc, attr_name) or []

        if len(old_closure) != len(new_closure):
            notify_error('Closure count of: %s changed... Skipping.' % (oldfunc,))
            return oldfunc

        for old_cell, new_cell in zip(old_closure, new_closure):
            self._update(None, None, old_cell.cell_contents, new_cell.cell_contents)

        return oldfunc

    def _update_method(self, oldmeth, newmeth):
        """Update a method object."""
        # XXX What if im_func is not a function?
        if hasattr(oldmeth, 'im_func') and hasattr(newmeth, 'im_func'):
            self._update(None, None, oldmeth.im_func, newmeth.im_func)
        elif hasattr(oldmeth, '__func__') and hasattr(newmeth, '__func__'):
            self._update(None, None, oldmeth.__func__, newmeth.__func__)
        return oldmeth

    def _update_class(self, oldclass, newclass):
        """Update a class object."""
        olddict = oldclass.__dict__
        newdict = newclass.__dict__

        oldnames = set(olddict)
        newnames = set(newdict)

        for name in newnames - oldnames:
            setattr(oldclass, name, newdict[name])
            notify_info0('Added:', name, 'to', oldclass)
            self.found_change = True

        # Note: not removing old things...
        # for name in oldnames - newnames:
        #    notify_info('Removed:', name, 'from', oldclass)
        #    delattr(oldclass, name)

        for name in (oldnames & newnames) - {'__dict__', '__doc__'}:
            self._update(oldclass, name, olddict[name], newdict[name], is_class_namespace=True)

        old_bases = getattr(oldclass, '__bases__', None)
        new_bases = getattr(newclass, '__bases__', None)
        if str(old_bases) != str(new_bases):
            notify_error('Changing the hierarchy of a class is not supported. %s may be inconsistent.' % (oldclass,))

        self._handle_namespace(oldclass, is_class_namespace=True)

    def _update_classmethod(self, oldcm, newcm):
        """Update a classmethod update."""
        # While we can't modify the classmethod object itself (it has no
        # mutable attributes), we *can* extract the underlying function
        # (by calling __get__(), which returns a method object) and update
        # it in-place.  We don't have the class available to pass to
        # __get__() but any object except None will do.
        self._update(None, None, oldcm.__get__(0), newcm.__get__(0))

    def _update_staticmethod(self, oldsm, newsm):
        """Update a staticmethod update."""
        # While we can't modify the staticmethod object itself (it has no
        # mutable attributes), we *can* extract the underlying function
        # (by calling __get__(), which returns it) and update it in-place.
        # We don't have the class available to pass to __get__() but any
        # object except None will do.
        self._update(None, None, oldsm.__get__(0), newsm.__get__(0))

    def _update_callable(self, oldcb, newcb):
        """
        Update a callable object, this object may contains one or many
        functions. But for performance issue, we only update first level
        of object's dict.
        """
        if not hasattr(oldcb, "__dict__") or not hasattr(newcb, "__dict__"):
            return
        olddict = oldcb.__dict__
        newdict = newcb.__dict__

        oldnames = set(olddict)
        newnames = set(newdict)

        for name in newnames - oldnames:
            setattr(oldcb, name, newdict[name])
            notify_info0('Added:', name, 'to', oldcb)
            self.found_change = True

        # Note: not removing old things...
        # for name in oldnames - newnames:
        #    notify_info('Removed:', name, 'from', oldclass)
        #    delattr(oldclass, name)

        for name in (oldnames & newnames) - {'__dict__', '__doc__'}:
            self._update(oldcb, name, olddict[name], newdict[name])

        # self._update_class(type(oldcb), type(newcb))
