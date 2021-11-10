"""
title: 剪绳子2
writer: 山客
date: 2021.4.5
example:
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 1
        mod = 1_000_000_007

        if n <= 3:
            return n - 1

        # 根据数学推论可知，以每段为3的分法所得乘积是最大的
        # a为所分段数，b为总长/3的余数
        b = n % 3
        a = n // 3

        for i in range(a - 1):
            # 由于引入了模的概念，所以  每一次方都必须确保没有越界
            res = res * 3 % mod

        if b == 0:
            res = res * 3
        elif b == 1:
            res = res * 4
        elif b == 2:
            res = res * 3 * 2

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(120))