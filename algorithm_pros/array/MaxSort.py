"""
title: 最大数
writer: 山客
date: 2021.11.9
key：快排即可
example:
输入:
[30, 1]
输出: "301"
解释: 301是该数组可以组合的最大值，题目要以string形式输出
"""


class cmp(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def solve(self, nums: list) -> str:
        # write code here
        strs = map(str, nums)

        strs = sorted(strs, key=cmp)

        if strs[0] == '0':
            return '0'
        else:
            return ''.join(strs)
