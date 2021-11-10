"""
title：摩斯电码解码
writer：山客
date：2021.8.21
key：动态规划
example：
输入：
11
输出：
2
tips：
① 注意 '1' 时的组合翻译方式
② 41 / 50 ？？？
"""


def MorseCode(n: list):
    l = len(n)
    dp = [0] * (l + 1)
    dp[l] = 1  # 最后一个字符只有一种翻译方式

    for i in range(l - 1, -1, -1):
        dp[i] = dp[i + 1]  # 至少有一种单个翻译方式
        # 若为 '1'且当前遍历长度大于等于2，还有组合翻译方式
        if n[i] == '1':
            if i + 2 <= l:  # 双字符码
                dp[i] += dp[i + 2]
            if i + 3 <= l:  # 三字符码
                dp[i] += dp[i + 3]
        dp[i] %= 2147483647

    return dp[0]


if __name__ == '__main__':
    n = list(input())

    res = MorseCode(n)
    print(int(res))
