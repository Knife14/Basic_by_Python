"""
title: 字符串的排列
writer: 山客
date: 2021.3.24
example:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""


class Solution:
    def permutation(self, s: str) -> list[str]:
        result = []

        if len(s) <= 1:
            return list(s)

        for i in range(len(s)):
            if s[i] not in s[:i]:
                # 取出的元素与之前取出的元素不得相同
                # 然后与剩下的字符全排列即可，递归迭代
                for j in self.permutation(s[:i] + s[i+1:]):
                    result.append(s[i] + j)

        return result