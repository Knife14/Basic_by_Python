"""
title：寻找旋转排序数组中的最小值②
writer：山客
date：2021.4.8
problem：有重复数值
example：
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组
"""

class Solution:
    def findMin(self, nums: list) -> int:

        m, n = 0, len(nums) - 1

        while m < n:
            # 二分法
            # 由于原数组是有序的，所以其实只需要从一个方向辨别即可
            # 以下是从最右端开始判断

            pivot = m + (n - m) // 2  # 在[m，n]中寻找新的二分区间

            if nums[pivot] < nums[n]:
                n = pivot
            elif nums[pivot] > nums[n]:
                m = pivot + 1
            else:
                # 相等的情况下，n继续往左移动
                n -= 1

        return nums[m]