"""
title: 斐波那契数列
writer: 山客
date: 2021.3.30
Key：动态规划
example:
输入：n = 2
输出：1

输入：n = 5
输出：5
thinking：
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
tips：
① 状态转换公式：dp[n] = dp[n - 1] + dp[n - 2]
② 符合这个公式的，都可以使用动态规划来做。
"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        
        return b % (1_000_000_007)





