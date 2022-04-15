"""
title: 股票的最大利润
writer: 山客
date: 2021.7.29
example:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

# 普通写法
# 时间复杂度：O（N）   空间复杂度：O（N）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 1)  # 记录当前价格位之前所能获得的最大利润

        cost = 1_000_000_009
        for i in range(1, len(prices) + 1):
            cost = min(cost, prices[i - 1])  # 动态更新最低买入花销
            dp[i] = max(dp[i - 1], prices[i - 1] - cost)  # 当前之前最大利润 与 当前价位 - 当前最低花销 作比较

        return dp[-1]

# 最优写法
# 时间复杂度： O（N）  空间复杂度： O（1）
class Solution:
    def maxProfit(self, prices: list) -> int:
        cost, profit = 1_333_333, 0

        for price in prices:
            cost = min(price, cost)
            profit = max(profit, price - cost)

        return profit
