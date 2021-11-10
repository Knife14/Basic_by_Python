"""
title：最长回文串
writer：山客
date：2021.8.26
key：贪心
example：
输入: "abccccdd"
输出: 7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
tips：
① 要考虑奇数位
"""

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0

        for v in cnt.values():
            ans += v // 2 * 2
            # 考虑奇数位，可以放在回文串的中间
            # 前提是当前回文串是偶数长度的，若已经是奇数长度，则不再添加
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1

        return ans
