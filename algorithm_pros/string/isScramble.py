"""
title：扰乱字符串
writer：山客
date：2021.4.16
key：分治、动态规划
example：
输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：
第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
tips：
① 和谐：两个字符串，即s1和s2互为扰乱字符串，即为和谐的。
"""

from collections import Counter
from functools import lru_cache as cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        # 缓存模块
        @cache(100)
        def DFS(l1: int, l2: int, length: int) -> bool:
            # 第一个字符串从l1开始
            # 第二个字符串从l2开始

            # 判断两个子串是否相等
            if s1[l1: l1 + length] == s2[l2: l2 + length]:
                return True

            # 判断是否存在字符c在两个子串中的出现的次数不同
            if Counter(s1[l1: l1 + length]) != Counter(s2[l2: l2 + length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换
                if DFS(l1, l2, i) and DFS(l1 + i, l2 + i, length - i):
                    return True
                # 交换
                if DFS(l1, l2 + length - i, i) and DFS(l1 + i, l2, length - i):
                    return True

            return False

        res = DFS(0, 0, len(s1))
        DFS.cache_clear()

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("a", "a"))




