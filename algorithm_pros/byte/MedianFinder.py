"""
title: 数据流中的中位数
writer: 山客
date: 2021.4.14
Key：
example：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
tips：
① 数组直接排序会超时
② 避免超时，使用大顶栈、小顶栈
"""

# heapq是小顶堆模块
from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []  # 小顶堆，保存较大的一半，根节点存放最小的大堆数
        self.B = []  # 大顶堆，保存较小的一半，根节点存放最大的小堆数

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            # 小顶堆正常存放
            # 实现大顶堆，可以将插入值取反
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        # 大顶堆取反
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
