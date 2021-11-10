"""
title：搜索旋转排序数组②
writer：山客
date：2021.4.7
example：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
"""


class Solution:
    def search(self, nums: list, target: int) -> bool:

        for i in range(len(nums)):
            if nums[i] == target:
                return True

        return False
