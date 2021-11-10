"""
title: 在排序数组中查找数组I
writer: 山客
date: 2021.4.18
example:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
"""


class Solution:
    def search(self, nums: list, target: int) -> int:
        times = 0

        for i in nums:
            if i == target:
                times += 1

        return times