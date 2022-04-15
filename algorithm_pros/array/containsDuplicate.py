"""
title：存在重复元素
writer：山客
date：2021.4.17
example：
输入: [1,2,3,1]
输出: true

输入: [1,2,3,4]
输出: false
"""

from collections import Counter


class Solution:
    def containsDuplicate(self, nums: list) -> bool:

        if not nums:
            return False

        tmp = Counter(nums)

        for k, v in tmp.items():
            if v > 1:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
