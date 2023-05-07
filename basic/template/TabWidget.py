# -*- coding: utf-8 -*- #

# -----------------------------
# Topic: base widget class
# Author: yang chaohuan
# Created: 2023.05.07
# Description: the base class about widget
# History:
# <autohr>    <version>    <time>        <desc>
#  motm14       v0.1    2022/09/22    basic build
#    m14        v0.2    2023/05/07    complete build as a template
# -----------------------------


from PySide6.QtWidgets import QTabBar, QTabWidget, QDialog, QVBoxLayout, QWidget, QMenuBar
from PySide6.QtGui import QMouseEvent, QMoveEvent, QCloseEvent
from PySide6.QtCore import Qt, QPoint, QEvent, Signal, Slot


class SETabBar(QTabBar):
    sig_drag_index = Signal(int)
    sig_drag_out_tab = Signal()
    
    def __init__(self, parent):
        super().__init__(parent)
    
        self.drag_start_pos = None
        self.____is_pressed__ = False
    
    def mousePressEvent(self, event: QMouseEvent):
        if self.____is_pressed__:
            event.ignore()
        
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.pos()
            self.____is_pressed__ = True
        return super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent):
        """
        
        drag tab widget
        
        """
        if abs(self.drag_start_pos.y() - event.pos().y()) > self.height():
            self.sig_drag_index.emit(self.currentIndex())
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        """
        
        when releasing mouse, check the drag distance.
        if drag distance is bigger than tabbar height, the widget should be dragged out.

        """
        self.____is_pressed__ = False
        if event.button() == Qt.LeftButton:
            if abs(self.drag_start_pos.y() - event.pos().y()) > self.height():
                self.sig_drag_out_tab.emit()
        return super().mouseReleaseEvent(event)


class SETabDialog(QDialog):
    sig_drag_widget = Signal(object, QPoint)
    sig_restore_widget = Signal(object)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.content = None
        self.toolbar = None
        self.ontop_action = None
    
    def set_content_widget(self, widget, label):
        self.setWindowTitle(label)
        self.content = widget
        self.content.setWindowTitle(label)
        
        new_layout = QVBoxLayout()
        new_layout.addWidget(self.content)
        new_layout.setStretch(1, 1)
        self.setLayout(new_layout)
        
        self.setMaximumSize(1080, 640)
        self.setMinimumSize(640, 480)
    
    def event(self, event: QEvent):
        if isinstance(event, QMoveEvent):
            self.sig_drag_widget.emit(self, event.pos())
        if isinstance(event, QCloseEvent):
            self.sig_restore_widget.emit(self.content)
        return super().event(event)


class SETabWidget(QTabWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setTabPosition(QTabWidget.South)

        self._drag_index = None
        self._drag_label = None
        self._drag_widget = None
        
        tabbar = SETabBar(self)
        self.setTabBar(tabbar)
        
        tabbar.sig_drag_index.connect(self.drag_index)
        tabbar.sig_drag_out_tab.connect(self.drag_out_tab)
    
    def append_normal_tab(self, widget: QWidget):
        if not widget:
            return
        
        widget.setAttribute(Qt.WA_DeleteOnClose)
        index = self.addTab(widget, widget.windowTitle())
        self.setCurrentIndex(index)
        
        return index
    
    @Slot(int)
    def drag_index(self, index):
        self._drag_index = index
        self._drag_label = self.tabText(index)
        self._drag_widget = self.widget(index)
    
    @Slot()
    def drag_out_tab(self):
        new_widget = SETabDialog(self.parentWidget())
        new_widget.setAttribute(Qt.WA_DeleteOnClose)
        if self._drag_widget:
            new_widget.set_content_widget(self._drag_widget, self._drag_label)
            new_widget.sig_drag_widget.connect(self.drag_back_tab)
            new_widget.sig_restore_widget.connect(self.append_normal_tab)
            new_widget.show()
            self._drag_widget.show()
            self.removeTab(self._drag_index)

    @Slot(object, QPoint)
    def drag_back_tab(self, dialog, pos):
        tab_bar = self.tabBar()
        bar_pos = tab_bar.mapFromGlobal(pos)
        if tab_bar.contentsRect().contains(bar_pos):
            widget = dialog.content
            index = self.append_normal_tab(widget)
            dialog.disconnect()
            dialog.close()
