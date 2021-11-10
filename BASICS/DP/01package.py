"""
title：01背包
writer：山客
date：2021.8.16
thinking：
① vi 表示第 i 个物品的价值 （ value ）
   wi 表示第 i 个物品的权重 （ weight ）
   V  表示背包总容量
   V(i, j) 表示当前背包容量为 j，前 i 个物品最佳组合对应的价值
② 递推式：面对当前商品只有两种可能性
    a. j < w[i] 即当前物品权重比背包容量大，装不下
      则 V(i, j) = V(i - 1, j)
    b. j >= w[i] 即当前背包还能放下当前物品，需要作优化处理判断最大价值
      则 V(i, j) = max(V(i - 1, j), V(i - 1, j - w[i]) + v[i])
improving：
① 一维推广：
    for i in range(n):
        for j in range(m, w[i] - 1, -1):
            V(j) = max(V(j - 1), V(j - w[i]) + v[i])
② 最优解详情：目前只能算出最优值大小（放入伪代码，无法直接使用）
    findPath(i, j):  # 从后往前
        if i >= 0:
            if dp[i][j] == dp[i - 1][j]:
                item[i] = 0
                findPath(i - 1, j)
            elif j - w[i] >= 0 and \
                dp[i][j] = dp[i - 1][j - w[i]] + v[i]:
                item[i] = 1
                findpath(i - 1, j - w[i])
    return item
"""


def _01PackageMAX(n: int, m: int, v: list, w: list):
    dp = [[0] * (m + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m + 1):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

    # print(dp)
    return dp


if __name__ == '__main__':
    n, m = 5, 8  # n - 数量， m - 背包总容量

    v = [0, 3, 4, 5, 6]  # 物品对应价值
    w = [0, 2, 3, 4, 5]  # 物品对应权重

    MAX_Matrix = _01PackageMAX(n, m, v, w)
    MAX = MAX_Matrix[-1][-1]
    print(MAX)
