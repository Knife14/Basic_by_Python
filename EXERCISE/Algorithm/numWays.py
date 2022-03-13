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
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        
        return b % (10 ** 9 + 7)

