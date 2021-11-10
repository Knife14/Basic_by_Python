"""
title: 1加到100
writer: 山客
date: 2021.8.24
Key: 线程（threading）
Problems:
① 未得到解决，输出无果
"""

import _thread
import time


def OneHundred(threadName: str, delay: int):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


if __name__ == '__main__':
    try:
        """
        _thread.start_new_thread(OneHundred, ())
        _thread.start_new_thread(OneHundred, ())
        _thread.start_new_thread(OneHundred, ())
        _thread.start_new_thread(OneHundred, ())
        _thread.start_new_thread(OneHundred, ()) 
        """
        _thread.start_new_thread(OneHundred, ("Thread-1", 2,))
        _thread.start_new_thread(OneHundred, ("Thread-2", 4,))
    except:
        print("Error: 无法启动线程")
