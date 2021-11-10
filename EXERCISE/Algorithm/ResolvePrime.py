"""
title：分解质因数
writer：山客
date：2021.9.6
key：
example：
输入：
100
输出：
[2,2,5,5]
tips：
① 直接检索时长较大 1600ms+
② 优化时长： 40ms
    import math
    MAX = math.sqrt(n)
    while i <= MAX:
        ...
    if n != 1:
        res.append(n)
"""


class Solution:
    def primeFactorization(self, n):
        # write code here
        res = []
        i = 2  # 质因数从 2 开始

        while n > 1:
            # 能被除尽，即当前 n 不是质数
            if n % i == 0:
                res.append(i)
                n //= i
            else:
                # 被 2 除完后，所有更大的偶数都将不作为需求值加入到res中
                # 由此类推，小质数除尽后，整数倍的大合数也不会被计算在内
                i += 1

        return res
