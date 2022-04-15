"""
title：方格游戏方案数量
writer：山客
date：2021.8.16
key：动态规划
example：
输入：
1
6 6
4 5 6 6 4 3
2 2 3 1 7 2
1 1 4 6 2 7
5 8 4 3 9 5
7 6 6 2 1 5
3 1 1 3 7 2
输出：
3948
tips：
"""


# 右下 -> 左上
def CheckGame1(n: int, m: int, energy: list):
    path = [[0] * m for _ in range(n)]
    psum = [[0] * m for _ in range(n)]

    # 从右下角遍历到左上角
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == n - 1 and j == m - 1:
                path[i][j] = 1
                psum[i][j] = 1
            else:
                # 横向
                start = j + 1
                end = start + energy[i][j]  # 能量可供当前行最远距离（水平向）
                # 防止越界
                if start < m and end < m:
                    path[i][j] += (psum[i][start] - psum[i][end])
                elif start < m:
                    path[i][j] += psum[i][start]

                # 纵向
                start = j
                for k in range(i + 1, i + 1 + energy[i][j]):
                    if k < n:
                        end -= 1
                        if end < m:
                            path[i][j] += (psum[k][start] - psum[k][end])
                        else:
                            path[i][j] += psum[k][start]
                if j + 1 < m:
                    psum[i][j] = path[i][j] + psum[i][j + 1]
                else:
                    psum[i][j] = path[i][j]

    return path[0][0] % 10_000


# 左上 -> 右下
def CheckGame2(n: int, m: int, energy: list):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if energy[i][j] <= 0:
                continue
            for a in range(energy[i][j] + 1):
                b = 0
                # 从纵向一直遍历到横向，所有可能
                while a + b <= energy[i][j]:
                    if a == 0 and b == 0:
                        b += 1
                        continue
                    if a + i < n and b + j < m:
                        dp[i + a][j + b] += dp[i][j]
                    b += 1

    return dp[-1][-1] % 10_000


if __name__ == '__main__':
    T = int(input())  # T 组测试数据

    for _ in range(T):
        lc = list(map(int, input().split()))  # n 行 m 列
        energy = []
        for i in range(lc[0]):
            energy.append(list(map(int, input().split())))

        res = CheckGame2(lc[0], lc[1], energy)
        print(res)
