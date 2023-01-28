"""
title：无重复字符的最长子串
writer：m14
date：2023.1.28
key：滑动窗口
example：
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sliding_window = []
        for tmp in s:
            if tmp in sliding_window:
                sliding_window = sliding_window[sliding_window.index(tmp) + 1:]
            sliding_window.append(tmp)
            max_len = max(max_len, len(sliding_window))
        
        return max_len


a = Solution()
s = "pwwkew"
print(a.lengthOfLongestSubstring(s))
