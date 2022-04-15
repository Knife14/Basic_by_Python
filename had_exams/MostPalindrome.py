"""
title：最多的回文
writer：山客
date：2021.8.21
key：
example：
输入：
abbcbb
输出：
4
tips：
"""


def MostPalindrome(s: str):
    if len(s) <= 1:
        return 0

    cnt = 0
    for i in range(len(s)):
        # 居中一个字符
        l = i - 1
        r = i + 1
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        # 居中两个字符
        l = i
        r = i + 1
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1

    return cnt


if __name__ == '__main__':
    s = input()

    res = MostPalindrome(s)
    print(res)
