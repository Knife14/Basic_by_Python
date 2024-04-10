"""
title: 正整数和负整数的最大计数
writer: m14
date: 2024.4.10
key：二分查找可以实现O(log n)时间复杂度
example:
输入：nums = [-2,-1,-1,1,2,3]
输出：3
解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
thinking：
"""


class Solution:
    def maximumCount_basic(self, nums: List[int]) -> int:
        n = len(nums)
        left_l, right_r = 0, n - 1
        mid = left_r = right_l = n // 2  # mid

        if nums[mid] == 0:
            while left_r >= 0 and nums[left_r] == 0:
                left_r -= 1
            while right_l < n and nums[right_l] == 0:
                right_l += 1
            return max(left_r - left_l + 1, right_r - right_l + 1)
        else:
            if nums[mid] > 0:
                while mid >= 0 and nums[mid] > 0:
                    mid -= 1
                return n - mid - 1
            else:
                while mid < n and nums[mid] < 0:
                    mid += 1
                return mid
    
    def maximumCount_advanced(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        # to find the first num which is bigger than 0 as r
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid

        while l > 0 and nums[l - 1] == 0:
            l -= 1
        
        return max(l, len(nums) - r)
