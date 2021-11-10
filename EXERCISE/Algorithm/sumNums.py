"""
title: 求和
writer: 山客
date: 2021.4.19
example:
输入: n = 3
输出：6

输入：n = 9
输出：45
"""

class Solution:
    def sumNums(self, n: int) -> int:
        return (1 + n) * n // 2