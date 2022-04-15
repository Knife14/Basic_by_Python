"""
title：二分查找
writer：山客
date：2021.7.20
example：
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -10
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            curr = left + (right - left) // 2
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                left = curr + 1
            else:
                right = curr - 1
        
        return -1