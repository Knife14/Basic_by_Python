"""
title：神奇矩阵
writer：山客
date：2021.8.11
key：动态规划
example：
输入：
5
5 9 5 4 4
4 7 4 10 3
2 10 9 2 3
输出：
5
tips：
① 进行动态规划时，要注意列与列之间的关系
"""


def MagicMatrix(n:int, data: list):
    dp = [[0, 0, 0]]

    # dp[i] = dp[i - 1] + min(|data[l][c] - data[:3][c - 1]|)
    for c in range(1, n):  # 列
        delta = []
        # 求出 dp[l][c] 的最小值
        # 即 在 dp[c - 1]的基础上，求出 data[:3][c] 与 dp[c] 的最小值关系
        # 遍历依次得 min(dp[c][:3])
        for l in range(3):  # 行
            d0 = abs(data[l][c] - data[0][c - 1]) + dp[-1][0]
            d1 = abs(data[l][c] - data[1][c - 1]) + dp[-1][1]
            d2 = abs(data[l][c] - data[2][c - 1]) + dp[-1][2]
            delta.append(min(d0, d1, d2))
            # print(delta)
        dp.append(delta)

    return min(dp[-1])


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(3):
        data.append(list(map(int, input().split())))

    print(MagicMatrix(n, data))
