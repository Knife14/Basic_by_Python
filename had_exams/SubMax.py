"""
title：子串的最大值
writer：山客
date：2021.11.9
key：
example：
输入：
'321', 2
输出：
32
tips：
"""


class Solution:
    def maxValue(self, s, k):
        # write code here
        l = len(s)
        maxNum = -1

        if l == k:
            return int(s)

        for i in range(0, l - k + 1):
            maxNum = max(maxNum, int(s[i: i + k]))

        return maxNum


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue('321', 2))
