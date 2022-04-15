"""
title：视力表
writer：山客
date：2021.8.14
key：求排列数
example：
输入：
2 3 1 0 0
输出：
12
tips：
"""

import math


def VisualChart(n: int, data: list):
    SIZE = n ** 2  # 视力表规格 n 行 n 列
    res = 1

    if SIZE == 0:
        return 0

    for m in data[: -1]:
        # 排列 A 公式
        res *= math.factorial(SIZE) // (math.factorial(m) * math.factorial(SIZE - m))
        SIZE -= m

    # 998244353 常用于计数取模
    return res % 998244353


if __name__ == '__main__':
    cin = list(map(int, input().split()))
    n = cin[0]  # 视力表规格 n 行 n 列
    data = cin[1:]  # 向上向下向左向右符号总数

    res = VisualChart(n, data)
    print(res)
