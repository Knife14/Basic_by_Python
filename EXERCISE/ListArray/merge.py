"""
title: 合并两个有效数组
writer: 山客
date: 2021.4.5
example:
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
thinking：
①也可用双指针的办法
"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 避免 m == 0，合并这样写
        for i in range(n):
            nums1[i + m] = nums2[i]

        # 合并后可以直接排序，但也可以额外使用别的排序方法，提高效率
        nums1.sort()
