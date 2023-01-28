"""
title: 三数之和
writer: knife14
date: 2023.1.28
key: 三指针
example:
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
tips:
1. 去重的关键解决办法就是先排序，然后遍历时遇到相同元素直接跳过
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            k = len(nums) - 1
            for j in range(i + 1, len(nums) - 1):
                # 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                while k > j and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append(nums[i], nums[j], nums[k])
            
        return res
         

a = Solution()
nums = [0,0,0,0]
print(a.threeSum(nums))
