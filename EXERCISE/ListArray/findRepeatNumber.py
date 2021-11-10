"""
title：数组中重复的数字
writer：山客
date：2021.3.29
example：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""


class Solution:
    def findRepeatNumber(self, nums: list) -> int:

        hashmap = {}   # 哈希表，记录出现过的数字

        for i in nums:
            if i in hashmap:
                # 如果已经出现过，即返回
                return i
            hashmap[i] = 1
