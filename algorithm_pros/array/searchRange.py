"""
title: 在排序数组中查找元素的第一个和最后一个位置
writer: knife14
date: 2023.1.30
key: 二分法
example:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3, 4]
tips: 
1. 时间复杂度O（logn）
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        index = -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        if index == -1:
            return [-1, -1]
        
        # 先确认数组中有target这个值，然后根据二分法找到的索引进行左右遍历
        left, right = index, index
        while nums[left] == target:
            if left - 1 >= 0 and nums[left - 1] == target:
                left -= 1
            else:
                break
        while nums[right] == target:
            if right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            else:
                break
        return [left, right]
        

a = Solution()
n = [5,7,7,8,8,10]
print(a.searchRange(n, 8))
