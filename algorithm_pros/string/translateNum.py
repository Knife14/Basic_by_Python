"""
title：把数组翻译成字符串
writer：山客
date：2021.7.29
key：动态规划
example：
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
tips：
① 设计动态规划的时候，要理解翻译方案的意思
    到第 i 个字符时，翻译方案并不是 dp[i] += dp[i - 1]
    而是dp[i] = dp[i - 1]，
    则若每个数字都独立翻译成一个英文字母，它们的方案数不增加
"""


class Solution:
    def translateNum(self, num: int) -> int:
        str_n = str(num)
        l = len(str_n)

        dp = [1] * l

        for i in range(1, l):
            tmp = str_n[i - 1: i + 1]
            # 若两个字符满足条件
            # 则要考虑 dp[i - 2] 的结果（往前推两个字符的结果数）
            # 与 dp[i - 1]（往前推一个字符）结果综合和
            if tmp >= "10" and tmp <= "25":
                dp[i] = dp[i - 2] + dp[i - 1]
            # 否则方案数与 dp[i - 1] 的情况相同
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.translateNum(12358))
