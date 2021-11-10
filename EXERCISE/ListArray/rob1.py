"""
title: 打家劫舍
writer: 山客
date: 2021.4.15
key：动态规划
example：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

"""


class Solution:
    def rob(self, nums: list) -> int:
        if not nums:
            return 0

        l = len(nums)
        if l == 1:
            return nums[0]

        dp = [0] * l
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, l):
            # 不能抢前一个的，所以比较的是dp[i - 2] + nums[i], dp[i - 1]
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp.pop()
