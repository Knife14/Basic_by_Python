"""
title: 0~n-1中缺失的数字
writer: 山客
date: 2021.4.18
example:
输入: [0,1,3]
输出: 2

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""


class Solution:
    def missingNumber(self, nums: list) -> int:

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i

        return len(nums)