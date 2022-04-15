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

# 递归
# 空间复杂度：O（N）    时间复杂度：O（N）
class Solution:
    def sumNums(self, n: int) -> int:
        if n == 1:
            return 1
        return n + self.sumNums(n - 1)
