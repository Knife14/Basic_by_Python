"""
title: 下一个排列
writer: knife14
date: 2023.1.30
key: 算法设计
example:
输入: nums = [1,2,3]
输出: [1,3,2]
tips: 
1. 找到一个一定大但变大幅度比较小的新序列；
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i指针先找到尽可能小的大数
        # 从右边开始找，就是为了将变大幅度尽可能减小
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # 如果 i 能找到，即当前序列不是降序
        # j指针找到与i指针最接近的小数，一样是为了控制变大幅度
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 交换完成后，原较大数右边的数需要按照升序重新排列。
        # 这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

a = Solution()
n = [1,2,3]
print(a.nextPermutation(n))
