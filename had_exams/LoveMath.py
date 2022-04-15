"""
title：小强爱数学
writer：山客
date：2021.8.14
key：数学公式，动态规划
example：
输入：
3
4 4 3
2 3 4
5 2 6
输出：
16
999999993
9009
tips：
① python 直接遍历求解会超时 4 / 10
"""


mod = 1_000_000_007


def LoveMath(data: list):
    A, B, n = data[0], data[1], data[2]  # A = x + y ; B = xy ; n 次方

    dp = [0] * (n + 1)
    dp[0], dp[1] = 2, A

    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        # 数学公式： Rn = a * Rn-1 - b * Rn-2
        for i in range(2, n + 1):
            dp[i] = (A * dp[i - 1] % mod - B * dp[i - 2] % mod + mod) % mod

    return dp[n]


if __name__ == '__main__':
    T = int(input())

    while T:
        data = list(map(int, input().split()))

        res = LoveMath(data)
        print(res)

        T -= 1
