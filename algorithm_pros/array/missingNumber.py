"""
title: 0~n-1中缺失的数字
writer: 山客
date: 2022.3.22
example:
输入: [0,1,3]
输出: 2

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""

# 只写了标记索引这么一种方法
# 时间复杂度： O（N）   空间复杂度： O（N）
class Solution:
    def missingNumber(self, nums: list) -> int:
        n = len(nums) + 1
        pointer = [0] * n

        for num in nums:
            pointer[num] = 1
        
        for i in range(n):
            if pointer[i] == 0:
                return i
