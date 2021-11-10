"""
title: 不用加减乘除做加法
writer: 山客
date: 2021.4.19
example:
输入: a = 1, b = 1
输出: 2
"""


class Solution:
    def no_oper_finish_add(self, a: int, b: int) -> int:
        mod = 0xffffffff
        # 取反码
        a, b = a & mod, b & mod

        while b != 0:
            # 异或运算
            # 按位与，左移一位
            a, b = a ^ b, (a & b) << 1 & mod

        if a <= 0x7fffffff:
            return a
        else:
            return ~(a ^ mod)
