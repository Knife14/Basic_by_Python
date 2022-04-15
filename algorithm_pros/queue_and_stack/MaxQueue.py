"""
title：队列的最大值
writer：山客
date：2021.7.29
example：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""

# 两数组，或两队列均可实现
class MaxQueue:

    def __init__(self):
        self.A = []
        self.B = []  # during all the time, making sure the max value in the first index

    def max_value(self) -> int:
        if self.B:
            return self.B[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.A.append(value)
        while self.B and self.B[-1] < value:
            self.B.pop()
        self.B.append(value)

    def pop_front(self) -> int:
        if not self.A:
            return -1
        tmp = self.A.pop(0)
        if tmp == self.B[0]:
            self.B.pop(0)
        
        return tmp

# 这个写法多少有点赖
import collections

class MaxQueue:

    def __init__(self):
        self.deque = collections.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
