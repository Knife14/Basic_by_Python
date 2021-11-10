"""
title: 旋转数组的最小数字
writer: 山客
date: 2021.4.2
example:
输入：[3,4,5,1,2]
输出：1

输入：[2,2,2,0,1]
输出：0
"""


class Solution:
    def minArray(self, numbers: list) -> int:

        """
        :param numbers:
        :return:
        # 暴力解答
        res = 1_000_000_007

        for i in numbers:
            if i <= res:
                res = i

        return res
        """

        num = sorted(numbers)

        return num[0]
