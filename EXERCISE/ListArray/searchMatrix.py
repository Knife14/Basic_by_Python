"""
title：搜索二维矩阵
writer：山客
date：2021.3.30
example：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
"""


class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target > matrix[i][n - 1]:
                continue
            else:
                if target in matrix[i]:
                    return True

        return False