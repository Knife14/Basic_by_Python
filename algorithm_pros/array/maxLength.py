"""
title: 最长无重复子数组
writer: 山客
date: 2021.8.26
Key：滑动窗口、队列均可做
problem：
输入：[2,3,4,5]
返回值：4
说明：[2,3,4,5]是最长子数组
tips：
① 暴力检索一定会超时，限制边界条件也不行
"""

from collections import deque


class Solution:
    def maxLengthbyDeque(self, arr):
        # write code here
        res = 0
        queue = deque()

        for curr in arr:
            while curr in queue:
                queue.popleft()
            queue.append(curr)
            res = max(res, len(queue))

        return res

    def maxLengthbyHash(self, arr):
        # 滑动窗口
        if len(arr) <= 1:
            return len(arr)

        l = -1  # 滑动窗口
        res = 0  # 比较最大值
        visited = {}  # 记录元素下标

        for r in range(len(arr)):
            if arr[r] in visited:
                l = max(l, visited[arr[r]])
            res = max(res, r - l)
            visited[arr[r]] = r

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxLengthbyDeque([1, 2, 3, 1, 2, 3, 2, 2]))
