"""
title: 按序打印
writer: 山客
date: 2021.3.23
Key: 线程（threading）、上下文管理器（with语句，代替try...excpet...finally...)
example:
输入: [1,2,3]
输出: "firstsecondthird"

输入: [1,3,2]
输出: "firstsecondthird"
"""

from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()  # 加锁，确保线程有序
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJobDone:
            printSecond()
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondJobDone:
            printThird()