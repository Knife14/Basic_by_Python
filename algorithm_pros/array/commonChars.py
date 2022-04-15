"""
title: 查找常用字符
writer: 山客
date: 2021.3.23
example:
输入：["bella","label","roller"]
输出：["e","l","l"]

输入：["cool","lock","cook"]
输出：["c","o"]
"""

from collections import Counter

class Solution:
    def commonChars(self, A: list[str]) -> list[str]:

        dp = Counter(A[0])

        for i in range(1, len(A)):
        	# 直接比对key
            dp &= Counter(A[i])

        return list(dp.elements())