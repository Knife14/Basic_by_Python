# -*- coding: utf-8 -*-

import logging

from PyQt5.QtWidgets import QTabBar, QTabWidget, QDialog, QVBoxLayout, QWidget, QMenuBar, QAction
from PyQt5.QtGui import QMouseEvent, QMoveEvent
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QPoint, QEvent


class TabBar(QTabBar):
    sig_drag_index = pyqtSignal(int)
    sig_drag_out_tab = pyqtSignal()
    
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
    
    def mouseMoveEvent(self, event):
        if self.tabText(self.currentIndex()) == '场景视图':
            return
        
        if abs(self.drag_start_pos.y() - event.pos().y()) > self.height():
            self.sig_drag_index.emit(self.currentIndex())
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if self.tabText(self.currentIndex()) == '场景视图':
            return
        
        self.____is_pressed__ = False
        if event.button() == Qt.LeftButton:
            if abs(self.drag_start_pos.y() - event.pos().y()) > self.height():
                self.sig_drag_out_tab.emit()
        return super().mouseReleaseEvent(event)


class TabDialog(QDialog):
    sig_drag_widget = pyqtSignal(object, QPoint)
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.____content__ = None
        self.toolbar = None
        self.ontop_action = None
    
    def set_content_widget(self, widget, label):
        widget.setWindowTitle(label)
        new_layout = QVBoxLayout()
        self.toolbar = QMenuBar(self)
        self.ontop_action = QAction('置顶')
        self.ontop_action.triggered.connect(self.set_ontop_state)
        self.toolbar.addAction(self.ontop_action)
        new_layout.addWidget(self.toolbar)
        new_layout.addWidget(widget)
        new_layout.setStretch(0, 0)
        new_layout.setStretch(1, 1)
        self.setLayout(new_layout)
        self.setMaximumSize(1080, 640)
        self.setMinimumSize(640, 480)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | 
                            Qt.CustomizeWindowHint)
        
        self.____content__ = widget
    
    @pyqtSlot()
    def set_ontop_state(self):
        action_text = self.ontop_action.text()
        window = self.windowHandle()
        if action_text == '置顶':
            window.setFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.ontop_action.setText('取消置顶')
        elif action_text == '取消置顶':
            window.setFlags(self.windowFlags())
            self.ontop_action.setText('置顶')
    
    @property
    def content(self):
        return self.____content__
    
    def event(self, event: QEvent):
        if isinstance(event, QMoveEvent):
            self.sig_drag_widget.emit(self, event.pos())
        return super().event(event)
    
        
class TabWidget(QTabWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self._drag_index = None
        self._drag_label = None
        self._drag_widget = None
        
        tabbar = TabBar(self)
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
    
    @pyqtSlot(int)
    def drag_index(self, index):
        self._drag_index = index
        self._drag_label = self.tabText(index)
        self._drag_widget = self.widget(index)
    
    @pyqtSlot()
    def drag_out_tab(self):
        new_widget = TabDialog(self.parentWidget())
        new_widget.setAttribute(Qt.WA_DeleteOnClose)
        if self._drag_widget:
            new_widget.set_content_widget(self._drag_widget, self._drag_label)
            new_widget.sig_drag_widget.connect(self.drag_back_tab)
            new_widget.show()
            self._drag_widget.show()
            self.removeTab(self._drag_index)

    @pyqtSlot(object, QPoint)
    def drag_back_tab(self, dialog, pos):
        tab_bar = self.tabBar()
        bar_pos = tab_bar.mapFromGlobal(pos)
        if tab_bar.contentsRect().contains(bar_pos):
            widget = dialog.content
            index = self.append_normal_tab(widget)
            dialog.disconnect()
            dialog.close()
