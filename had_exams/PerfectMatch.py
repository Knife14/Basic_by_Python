"""
title：完美对
writer：山客
date：2021.8.18
key：
example：
输入：
5 3
2 11 21
19 10 1
20 11 1
6 15 24
18 27 36
输出：
3
tips：
① 遍历差分求解
② 使用差分和求解，有可能会出现差分和结果一致，但具体差分情况不符合的例子  6 / 10
"""


def PerfectMatch(n: int, k: int, data: list):
    res = 0
    delta_map = {}

    for i in range(n):
        delta_list = []
        for j in range(1, k):
            delta_list.append(data[i][j] - data[i][j - 1])

        ostr = ''.join([str(d) for d in delta_list])  # 原差值
        nstr = ''.join([str(-d) for d in delta_list])  # 取反结果

        # 完美对数
        if nstr in delta_map:
            res += delta_map[nstr]

        if ostr not in delta_map:
            delta_map[ostr] = 1
        else:
            delta_map[ostr] += 1

    return res


if __name__ == '__main__':
    n = list(map(int, input().split()))  # n个物品，每个物品k个属性
    data = [[] for _ in range(n[0])]

    for i in range(n[0]):
        data[i] += list(map(int, input().split()))

    print(PerfectMatch(n[0], n[1], data))
