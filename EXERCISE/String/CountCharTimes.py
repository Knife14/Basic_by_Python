"""
title：字符串最后一个单词的长度
writer：山客
date：2021.9.17
problem：
输入：
ABCabc
A
输出：
2
"""

from collections import Counter


class Solution:
    def CountCharTimes(self, s: str, target: str) -> int:
        cnt = dict(Counter(s.lower()))

        if target.lower() in cnt.keys():
            return cnt[target.lower()]
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    m = input()
    t = input()
    print(s.CountCharTimes(m, t))
