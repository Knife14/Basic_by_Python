"""
title：数组中数字出现的次数
writer：山客
date：2021.7.20
example：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
"""

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        times = {}
        res = []

        for num in nums:
            if num not in times:
                times[num] = 1
            else:
                times[num] += 1
        
        for k, v in times.items():
            if v == 1:
                res.append(k)
        
        return res

        # {key:value, key:value}
                