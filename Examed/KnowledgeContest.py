"""
title：知识竞赛
writer：山客
date：2021.8.15
key：直接遍历需要考虑边界条件
example：
输入：
4
4 100
50 50
10000 10000
20000 20000
输出：
15000.0
tips：
① 直接遍历肯定超时 3 / 10
    所以要优化边界条件
"""


def KnowContest(n: int, data: list):
    data = sorted(data, key=lambda x: abs(x[0] - x[1]))  # x[0] + x[1] 排序时间会是其两倍
    print(data)

    MIN = 0  # 最小能力差
    for i in range(n - 1):
        j = i + 1
        # 两个 for 循环会超时，更改循环，添加边界条件
        while data[i][0] + data[i][1] + data[j][0] + data[j][1] > 4 * MIN:
            tmpA = (data[i][1] + data[j][1]) / 2
            tmpB = (data[i][0] + data[j][0]) / 2

            if min(tmpA, tmpB) > MIN:
                MIN = min(tmpA, tmpB)

            # j 有可能会越界
            if j + 1 < n:
                j += 1
            else:
                break

    return MIN


if __name__ == '__main__':
    n = int(input())  # 员工数
    data = [list(map(int, input().split())) for _ in range(n)]  # 能力详情

    res = KnowContest(n, data)
    print(res)
