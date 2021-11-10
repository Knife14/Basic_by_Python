"""
title：字符串最后一个单词的长度
writer：山客
date：2021.9.17
problem：
输入：
hello nowcoder
输出：
8
"""


class Solution:
    def LastWordLength(self, s: str) -> int:
        l = len(s)

        if l == 0:
            return 0

        for i in range(l - 1, -1, -1):
            if s[i] == ' ':
                return l - i - 1

        return l


if __name__ == '__main__':
    s = Solution()
    print(s.LastWordLength(input()))
