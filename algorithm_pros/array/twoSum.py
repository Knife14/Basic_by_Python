"""
title: 两数之和
writer: 山客
date: 2021.3.22
key：哈希表
example:
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res = []
        for index, num in enumerate(nums):
            if target - num in nums[index + 1:]:
                res.extend((index, nums[index + 1:].index(target - num) + index + 1))
                break
        
        return res

    def twoSumByHash(self, numbers: list, target: int) -> list:
        hashtable = dict()

        for i, num in enumerate(numbers):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[numbers[i]] = i

        return []

