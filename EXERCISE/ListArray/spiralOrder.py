"""
title：顺时针打印矩阵
writer：山客
date：2021.4.9
key：递归
example：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: list) -> list:

        res = []

        if not matrix or not matrix[0]:
            return res

        # m - 行， n - 列
        # left - 最左，right -最右，top - 顶层， bottom - 底层
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1

        while top <= bottom and left <= right:
            # 顺时针旋转，一个圈分成四部分
            for i in range(left, right + 1):
                # 上部
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                # 右部
                res.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left - 1, -1):
                    # 下部
                    res.append(matrix[bottom][i])
                for i in range(bottom - 1, top, -1):
                    # 左部
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res