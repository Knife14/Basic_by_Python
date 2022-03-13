"""
title: 单词长度的最大乘积
writer: 山客
date: 2021.11.11
Key：set、冒泡比较
problem：
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。
"""


class Solution:
    def maxProduct(self, words: list) -> int:
        sorted_words = sorted(words, key=len, reverse=True)  # 降序排序

        # 利用set不重复元素的特性存储数组
        Set_Words = []
        for word in sorted_words:
            Set_Words.append(set(word))

        # 冒泡比较
        l = len(words)
        res = 0
        for i in range(l - 1):
            # 优化遍历
            if res > len(sorted_words[i]) * len(sorted_words[i + 1]):
                break
            for j in range(i + 1, l):
                # 没有交集，即不包含相同字符
                if not (Set_Words[i] & Set_Words[j]):
                    res = max(res, len(sorted_words[i]) * len(sorted_words[j]))

        return res
