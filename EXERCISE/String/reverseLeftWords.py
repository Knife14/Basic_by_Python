"""
title: 翻转单词顺序
writer: 山客
date: 2021.4.19
example:
输入: s = "abcdefg", k = 2
输出: "cdefgab"
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s:
            return ""

        if not n % len(s):
            return s

        return s[n:] + s[:n]
