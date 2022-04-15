"""
title: 两数之和
writer: 山客
date: 2021.3.22
key：双指针、哈希表
example:
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]
"""


class Solution:
    def twoSumByPointer(self, nums: list, target: int) -> list:
        i, j = 0, len(nums) - 1
        res = []

        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == target:
                res.append(nums[i])
                res.append(nums[j])
                break
            elif tmp > target:
                j -= 1
            elif tmp < target:
                i += 1

        return res

    def twoSumByHash(self, numbers: list, target: int) -> list:
        hashtable = dict()

        for i, num in enumerate(numbers):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[numbers[i]] = i

        return []

