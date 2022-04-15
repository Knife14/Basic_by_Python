"""
title：最长不含重复字符的字符串
writer：山客
date：2021.7.29
example：
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :param s:
        :return:
        利用动态规划 + 双指针解答
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i -= 1 # 线性查找 i
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

        """
        ans = []

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            ans.append(1)
            tmp = {}
            tmp[s[i]] = 1
            for j in range(i + 1, len(s)):
                if s[j] not in tmp:
                    tmp[s[j]] = 1
                    ans[i] += 1
                else:
                    break

        ans = sorted(ans)

        return ans.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
