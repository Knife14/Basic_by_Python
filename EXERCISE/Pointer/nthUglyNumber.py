"""
title：丑数2：找出第n个丑数
writer：山客
date：2021.4.10
key：动态规划，指针
example：
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
tips：
① 丑数 是只包含质因数 2、3 和/或 5 的正整数。
② 1 通常被视为丑数。
③ 若每个都判断丑数，会导致超时。
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        # 定义三个指针
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            # 逐轮寻找最小的丑数
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)

            # 不能用elif，因为指针乘积有可能相等
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))