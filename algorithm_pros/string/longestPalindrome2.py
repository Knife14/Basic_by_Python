"""
title: 最长回文子串
writer: knife14
date: 2023.1.28
key: 动态规划
example:
输入: s = "babad"
输出: "bab"
解释: "aba" 同样是符合题意的答案。
tips:
1. 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串
"""

class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        begin = 0  # 最长回文子串头索引
        max_len = 1  # 最长回文子串长度
        # 构建动规矩阵，全部情况初始化为False
        dp = [[False] * len(s) for _ in range(len(s))]
        for _ in range(len(s)):
            dp[_][_] = True  # 每一个字符独立时都是回文串

        # 先枚举子串长度
        for subs_len in range(2, len(s) + 1):
            # 再确定子串左边界
            for i in range(len(s)):
                # 最后确定右边界，并防止右边界越界
                j = i + subs_len - 1
                if j >= len(s):
                    break

                # 判断回文成立
                if s[i] == s[j]:
                    dp[i][j] = True if j - i < 3 else dp[i + 1][j - 1]
                
                # 重新确定最长回文子串的索引与长度
                # 只要dp[i][j] == true，就表示子串 s[i: j] 是回文
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        
        return s[begin: begin + max_len]
     
    # 中心扩散，要分居中位是一个还是两个
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        res = ""
        for i in range(len(s)):
            # 居中一位
            l = i - 1
            r = i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1: r]
            # 居中两位
            l = i
            r = i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(res) < r - l - 1:
                res = s[l + 1: r]
        
        return res

a = Solution()
s = "babad"
print(a.longestPalindrome(s))
