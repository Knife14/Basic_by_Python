"""
title：正则表达式的匹配
writer：山客
date：2021.4.7
key：状态转移
example：
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
tips：
① . 表示任意一个字符， * 表示前面一个字符
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def match(i, j) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                # .* 情况下，返回true
                return True
            return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        # 状态矩阵, n+1行 m+1列 s、p位标对应1~m+1，1~n+1
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * 可表示为前一字符
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        # .* 情况下，返回true
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]

        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("ab", ".*"))
