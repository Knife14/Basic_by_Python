"""
title: 最长公共子序列（典型的二维动态规划问题）
writer: 山客
date: 2021.4.3
key：动态规划
example:
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
thinking：
①引入二维矩阵
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 判断到目前位置，已知的最长公共序列长度
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence("oxcpqrsvwf","shmtulqrypy"))
