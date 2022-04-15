"""
title: 圆圈中最后剩下的数字
writer: 山客
date: 2021.4.19
key：动态规划
example:
输入: n = 5, m = 3
输出: 3

输入: n = 10, m = 17
输出: 2
"""

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0

        for i in range(2, n + 1):
            x = (x + m) % i

        return x