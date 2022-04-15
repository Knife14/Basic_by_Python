"""
title：修水渠
writer：山客
date：2021.8.11
key：
example：
输入：
4
0 0
0 50
50 50
50 0
输出：
100
tips：
"""


def RepairCanals(x: list):
    x = sorted(x)
    l = len(x)
    mid = l // 2

    # 单数间房子，将以中间那一间为界，水渠穿过该房屋
    if l % 2:
        return sum(x[mid + 1:]) - sum(x[: mid])
    # 双数间房子，直接取中间
    else:
        return sum(x[mid:]) - sum(x[: mid])


if __name__ == '__main__':
    n = int(input())  # 一共 n 个房子
    location = []
    x, y = [], []

    for i in range(n):
        location.append(list(map(int, input().split())))

    for i in range(len(location)):
        x.append(location[i][0])
        y.append(location[i][1])

    print(RepairCanals(x))
