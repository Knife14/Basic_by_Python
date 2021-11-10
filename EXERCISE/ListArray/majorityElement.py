"""
title: 数组中出现次数超过一半的数字
writer: 山客
date: 2021.4.13
example:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
"""


class Solution:
    def majorityElement(self, nums: list) -> int:
        hash = {}
        l = len(nums)

        for i in range(l):
            if nums[i] in hash:
                hash[nums[i]] += 1
            else:
                hash[nums[i]] = 1

        for k, v in hash.items():
            if v > l // 2:
                return k