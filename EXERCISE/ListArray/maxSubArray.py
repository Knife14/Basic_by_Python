"""
title: 连续子数组的最大和
writer: 山客
date: 2021.4.14
key：动态规划
example：
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
tips：
① 暴力检索会超时
"""


class Solution:
    def maxSubArray(self, nums: list) -> int:

        for i in range(1, len(nums)):
            # 若nums[i - 1] <= 0，则nums[i] = nums[i]
            # 若nums[i - 1] > 0, 则nums[i] = nums[i] + nums[i - 1]
            nums[i] += max(nums[i - 1], 0)

        print(nums)
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
