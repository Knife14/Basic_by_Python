"""
title: 打印从1到最大的n位数
writer: 山客
date: 2021.4.5
example:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""


class Solution:
    def printNumbers(self, n: int) -> list:
        nums = []

        """
        l = 1
        for i in range(n):
            l *= 10
        l -= 1
        """

        for i in range(1, 10 ** n):
            nums.append(i)

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(2))