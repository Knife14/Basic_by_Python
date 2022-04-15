"""
title: 数值的整数次方
writer: 山客
date: 2021.4.5
key：快速幂（二进制角度）
example:
输入：x = 2.00000, n = 10
输出：1024.00000

输入：x = 2.10000, n = 3
输出：9.26100
thinking；
①幂的二进制展开：x^n = x^(1*b0+2*b1+4*b2+...+2^m-1*bm-1)
                      = x^(1 * b0) * x^(2 * b1) * ... * x ^(2^m-1 * bm-1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0 and x != 0:
            return 1

        if x == 0:
            return 0

        if n < 0:
            x, n = 1 / x, -n

        res = 1

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2, 10))
    print(s.myPow(2.1, 3))
    print(s.myPow(2, -2))