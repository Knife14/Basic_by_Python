"""
title：搜索旋转排序数组①
writer：山客
date：2021.4.7
example：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
tips：
①针对原有序排列数组，可以用二分法查找，时间复杂度是O(n)= nlogn
"""


class Solution:
    def search(self, nums: list, target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    # 二分法重新确定边界
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
