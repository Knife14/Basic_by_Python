"""
title：牛牛吃糖果
writer：山客
date：2021.8.16
key：01背包，动态规划
example：
输入：
3 10
5 1 5
1
1 3
输出：
2
tips：
① 此题的 v 是rcow，即牛的数量，背包容量是糖果数量 m
"""


def EatSugars(n: int, m: int, sugars: list, re: list):
    # 整合关系对与糖果的关系量，cnt - 牛数，sugars - 糖数
    cnt = [1] * n
    for a, b in re:
        cnt[a - 1] += 1
        cnt[b - 1] = 0
        sugars[a - 1] += sugars[b - 1]
        sugars[b - 1] = 0

    # 01背包问题
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(n):
        for j in range(m + 1):
            if j < sugars[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - sugars[i]] + cnt[i])

    return dp[-1][-1]


if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)  # n 牛 m 糖

    sugars = list(map(int, input().split()))

    k = int(input())  # k 关系对
    re = []
    for _ in range(k):
        re.append(list(map(int, input().split())))

    res = EatSugars(n, m, sugars, re)
    print(res)
