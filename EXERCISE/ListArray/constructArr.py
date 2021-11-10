"""
title：构建乘积数组
writer：山客
date：2021.7.29
example：
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""


class Solution:
    def constructArr(self, a: list) -> list:
        b, tmp = [1] * len(a), 1
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]  # 下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]            # 上三角
            b[i] *= tmp                # 下三角 * 上三角
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1,2,3,4,5]))
