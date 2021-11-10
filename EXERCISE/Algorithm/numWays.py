"""
title: 青蛙跳台阶
writer: 山客
date: 2021.4.2
key：斐波那契数列、动态规划
problem：
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
example:
输入：n = 7
输出：21
"""


class Solution:
    def numWays(self, n: int):

        mod = 1_000_000_007

        """
        # 递归不是不行，但是会超时
        if n == 0:
            return 0
        elif n <= 3:
            return n % mod
        else:
            return (self.numWays( n - 1) + self.numWays( n - 2)) % mod
        """

        a = b = 1  # 由于当台阶为0或1时，都返回1

        # 动态规划
        for i in range(n):
            a, b = b, a + b

        return a % mod

