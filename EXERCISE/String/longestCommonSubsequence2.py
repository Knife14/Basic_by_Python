"""
title: 最长公共子序列2（典型的二维动态规划问题）
writer: 山客
date: 2021.9.27
key：动态规划
example:
输入：text1 = "abcde", text2 = "ace"
输出：ace
解释：最长公共子序列是 "ace"  。

输入：text1 = "abc", text2 = "def"
输出：-1
解释：两个字符串没有公共子序列，返回 -1 。
thinking：
①引入二维矩阵
"""


class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str):
        if not s1 or not s2:
            return -1

        n, m = len(s1), len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 根据最长子序列长度找到对应位置的元素，并且添加到 res 中
        m_l = dp[-1][-1]  # 最长子序列长度
        i, j = n, m
        res = ''
        while m_l > 0:
            while i > 0 and dp[i - 1][j] == m_l:
                i -= 1
            while j > 0 and dp[i][j - 1] == m_l:
                j -= 1

            res += s1[i - 1]

            m_l -= 1
            i -= 1
            j -= 1

        if res:
            return ''.join(reversed(res))
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("1A2C3D4B56", "B1D23A456A"))
