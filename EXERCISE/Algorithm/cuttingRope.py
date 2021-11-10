"""
title: 剪绳子
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

import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 0

        if n <= 3:
            return n - 1

        # 根据数学推论可知，以每段为3的分法所得乘积是最大的
        # a为所分段数，b为总长/3的余数
        b = n % 3
        a = n // 3

        if b == 0:
            res = int(math.pow(3, a))
        elif b == 1:
            # 余数为1时，最后一段为4，乘积最大
            res = int(math.pow(3, a - 1) * 4)
        elif b == 2:
            # 余数为2时，最后一段为2，乘积最大
            res = int(math.pow(3, a) * 2)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(5))