"""
title：丑数
writer：山客
date：2021.4.10
example：
输入：n = 6
输出：true
解释：6 = 2 × 3

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。
tips：
① 丑数 是只包含质因数 2、3 和/或 5 的正整数。
② 1 通常被视为丑数。
"""


class Solution:
    def IsUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            # n 是丑数 = n能同时被 2、3、5（乱序）整除，最后仅剩下1。
            while n % factor == 0:
                n //= factor

        # 1 的时候也返回true
        return n == 1


if __name__ == '__main__':
    s = Solution()
    print(s.IsUgly(1))