"""
title：国际交流会
writer：山客
date：2021.8.11
key：二分、交叉插入（翻转、对称插入也可）
example：
输入：
4
3 6 2 9
输出：
20
6 2 9 3
tips：
① 直接用排列的话，会超时
"""


def InternationalExchange(n: int, data: list):
    data = sorted(data)  # 升序

    # 二分数组
    mid = n // 2
    mind = data[: mid]
    maxd = data[mid:]
    rlist = []

    # 交叉插入（对称插入也可）
    for i in range(mid):
        rlist.append(maxd[i])
        rlist.append(mind[i])

    # 若数组为单数，即大数组多1，所以要额外加大数组最后一个元素
    if n % 2:
        rlist.append(maxd[-1])

    # 求差异和
    res = 0
    for i in range(1, n):
        res += abs(rlist[i] - rlist[i - 1])
    res += abs(rlist[-1] - rlist[0])

    return res, rlist


if __name__ == '__main__':
    n = int(input())  # 与会人数 n
    data = list(map(int, input().split()))

    cnt, res = InternationalExchange(n, data)

    print(cnt)
    for i in range(n):
        print(res[i], end=' ')
