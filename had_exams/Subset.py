"""
title：子集
writer：山客
date：2021.8.14
key：x相同的情况下y更大的排序在前面（不然的话会重复统计相同的x），然后对y做一次最长上升子序列即可
example：
输入：
2
3
1 3 2
0 2 3
4
1 5 4 2
10 32 19 21
输出：
2
3
tips：
① cmp 排序会超时，可以更改为 key = (x[0], -x[1]) 与 cmp 排序意义一致
"""

from bisect import bisect_left
import functools


def tcmp(a: list, b: list):
    if a[0] == b[0]:
        return b[1] - a[1]
    return a[0] - b[0]


def Subset(n: int, data: list):
    data = sorted(data, key=functools.cmp_to_key(tcmp))

    total = 0
    res = [0] * 10
    for i in range(n):
        t = bisect_left(a=res, x=data[i][1], lo=0, hi=total)
        # 若插入到res的末端，则res长度 + 1，亦total + 1
        if t == total:
            total += 1
        res[t] = data[i][1]
        print(res)

    return total


if __name__ == '__main__':
    T = int(input())  # T 组数据

    while T > 0:
        n = int(input())  # n 个物品
        x = list(map(int, input().split()))  # 对应 x 属性
        y = list(map(int, input().split()))  # 对应 y 属性

        # 数据处理
        data = [[0, 0] for _ in range(n)]
        for i in range(n):
            data[i][0] = x[i]
            data[i][1] = y[i]

        print(Subset(n, data))

        T -= 1

