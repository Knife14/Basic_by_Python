"""
title：最长回文子串
writer：山客
date：2021.8.26
key：贪心，居中往左右遍历
example：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
tips：
① 边界条件顺序会影响解释器编译
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        l = len(s)
        res = ""

        for i in range(l):
            # 居中一个字符
            low = i - 1
            high = i + 1
            while low >= 0 and high <= l - 1 and s[low] == s[high]:  # 条件顺序会影响
                low -= 1
                high += 1
            if len(res) < (high - low - 1):
                res = s[low + 1: high]
            # 居中两个字符
            low = i
            high = i + 1
            while low >= 0 and high <= l - 1 and s[low] == s[high]:  # 条件顺序会影响
                low -= 1
                high += 1
            if len(res) < (high - low - 1):
                res = s[low + 1: high]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
