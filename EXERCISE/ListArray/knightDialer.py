"""
title: 骑士拨号器
writer: 山客
date: 2021.3.20
"""


class Solution:
    def knightDialer(self, n: int) -> int:
        # DP问题，逆推法，骑士走“日”
        dp = [[1 for i in range(10)] for i in range(n)]
        mod = 1_000_000_007
        for i in range(1, n):
            # 从1开始，到N结束，共n-1次循环
            # dp[i][x]为第i次的落点，dp[i-1][x]为第i-1的落点
            dp[i][0] = dp[i - 1][4] + dp[i - 1][6]
            dp[i][1] = dp[i - 1][6] + dp[i - 1][8]
            dp[i][2] = dp[i - 1][7] + dp[i - 1][9]
            dp[i][3] = dp[i - 1][4] + dp[i - 1][8]
            dp[i][4] = dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][9]
            dp[i][5] = 0
            dp[i][6] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][7]
            dp[i][7] = dp[i - 1][2] + dp[i - 1][6]
            dp[i][8] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][9] = dp[i - 1][2] + dp[i - 1][4]
            for j in range(10):
                dp[i][j] %= mod  # 取余，以保证不超出mod范围
        return sum(dp[n-1]) % mod