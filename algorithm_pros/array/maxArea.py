"""
title: 盛最多水的容器
writer: knife14
date: 2023.1.28
key: 
example:
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
tips:
1. 理清一个逻辑关系：
若向内 移动短板 ，水槽的短板可能变大，因此下个水槽的面积 可能增大 。
若向内 移动长板 ，水槽的短板不变或变小，因此下个水槽的面积 一定变小 。
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        
        # 只向内移动短板
        while left != right:
            if height[left] < height[right]:
                res = max(res, (right - left) * height[left])
                left += 1
            else:
                res = max(res, (right - left) * height[right])
                right -= 1
        
        return res

a = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(a.maxArea(height))
