"""
title：选择物品
writer：山客
date：2021.8.11
key：
example：
输入：
5 2
输出：
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
tips：
"""

import itertools


def Selection(n, m):
    data = [str(i + 1) for i in range(n)]

    if m == 1:
        for i in range(n):
            print(data[i])
    else:
        # 组合，非排列
        # 123、321、132等均作为同一方案
        for curr in itertools.combinations(data, m):
            print(' '.join(curr))


if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)

    Selection(n, m)
