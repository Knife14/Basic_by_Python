"""
title：替换空格
writer：山客
date：2021.3.29
example：
输入：s = "We are happy."
输出："We%20are%20happy."
"""

class Solution:
    def replaceSpace(self, s: str) -> str:

        res = ""
        s = list(s)

        for i in s:
            if i == ' ':
                i = "%20"
            res += i

        return res