"""
title: 和为s的连续正数序列
writer: 山客
date: 2021.4.18
key：滑动窗口，双指针
example:
输入：target = 9
输出：[[2,3,4],[4,5]]

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""

# 时间复杂度：O（N）    空间复杂度：O（1）
class Solution:
    def findContinuousSequence(self, target: int) -> list:
        mid  = target // 2

        res = []
        i, j, tmp = 1, 1, 0
        while i <= mid:
            if tmp < target:
                tmp += j
                j += 1
            else:
                if tmp == target:
                    res.append(list(range(i, j)))
                tmp -= i
                i += 1
        
        return res
