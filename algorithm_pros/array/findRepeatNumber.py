"""
title：数组中重复的数字
writer：山客
date：2021.3.29
example：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""

# 简单做法： 设置set()，遍历数组，将每个数值添加进set()中，直到发现有重复的为止。
# 时间复杂度： O（n）   空间复杂度： O（n）

# 原地交换
# 时间复杂度： O（n）   空间复杂度： O（1）
class Solution:
    def findRepeatNumber(self, nums: list) -> int:
        i = 0

        # we must to pay attention to the i's self increase
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            
            if nums[i] == nums[nums[i]]:
                return nums[i]
            
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
