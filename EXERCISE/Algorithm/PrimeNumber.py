"""
title：分解质因数
writer：山客
date：2021.9.17
problem：
输入：
180
输出：
2 2 3 3 5
"""

import math


class Solution:
    def PrimeNumber(self, num: int) -> list:
        res = []
        MAX = math.sqrt(num)
        i = 2  # 质因数从 2 开始

        # 边界条件：
        while i <= MAX:
            # 能被除尽，即当前 n 不是质数
            if num % i == 0:
                res.append(str(i))
                num //= i
            else:
                # 被 2 除完后，所有偶数都将不作为需求值加入到res中
                i += 1

        # 当前 n 还不是1，而是一个比1大的质数
        if num != 1:
            res.append(str(num))

        return res


if __name__ == '__main__':
    s = Solution()

    num = int(input())
    res = s.PrimeNumber(num)

    print(' '.join(res))
