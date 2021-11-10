"""
title: 最小的k个数
writer: 山客
date: 2021.4.13
example:
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

输入：arr = [0,1,2,1], k = 1
输出：[0]
"""


class Solution:
    def getLeastNumbers(self, arr: list, k: int) -> list:

        arr = sorted(arr)

        # 返回arr[0]~arr[k - 1]
        return arr[0:k]
