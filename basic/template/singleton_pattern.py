"""
title：单例模式
writer：山客
date：2022.3.23
content：一个类只有一个实例
tips：
① 还有更简单的写法（直接定义一个实例也算），如果不是多线程，可以不需要加锁。
② 或许python中有专门的库 / 方法可以实现单例模式。
③ 在不同文件下调用同一个实例，要注意调用顺序、调用路径。顺序应该是先改变实例的“调用”在前，路径应该保持一致（包括模块）
"""

from PyQt5.QtCore import QDir

from enum import Enum
import threading

# enum PointofView { Overhead, Near }
class PointofView(Enum):
    Overhead = 1
    Near = 2


class SingletonType(type):
    _instance_lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance

class WindowSetting(metaclass=SingletonType):

    def __init__(self):
        self.max_frame_num_ = 100
        self.file_root_path_ = QDir.toNativeSeparators(QDir.currentPath())  
        self.selected_item_ = None
        self.if_save_images_ = False
        self.camera_pos = [float(0), float(200), float(400), float(0), float(1000), float(0)]  # list(float)
        self.linear_speed = 50
        self.look_speed = 160
        self.playback_speed = 10
        self.if_save_layout_ = False
        self.img_size = 500
        self.if_keep_text_horizontal_ = False
        self.having_global_control = False

    def GetMaxFrameNum(self):
        return self.max_frame_num_
    
    def MaxFrameNumChange(self, num: int, file_root_path: str):
        self.max_frame_num_ = num
        self.file_root_path_ = file_root_path

WindowSettings = WindowSetting()

if __name__ == '__main__':
    w = WindowSetting()
    a = WindowSetting()
    print(w.if_save_images_)
    print(a.if_save_images_)
    w.if_save_images_ = True
    print(a.if_save_images_)
