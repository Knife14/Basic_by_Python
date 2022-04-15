"""
title：n个骰子的点数
writer：山客
date：2021.7.29
example：
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
"""


class Solution:
    def dicesProbability(self, n: int) -> list:
        dp = [1 / 6] * 6

        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)  # 一共有 5n + 1 种结果
            for j in range(len(dp)):
                for k in range(6):
                    # tmp[j + k] is according to the curr val of dp[j]
                    # and itself,
                    # because of j + k == the same value, 
                    # it maybe have many different answers...
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        
        return dp


if __name__ == '__main__':
    s = Solution()
    print(s.dicesProbability(2))
