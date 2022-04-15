"""
title: 第一个出现一次的字符
writer: 山客
date: 2021.4.18
example:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "

        count = {}

        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for k, v in count.items():
            if v == 1:
                return k

        return " "