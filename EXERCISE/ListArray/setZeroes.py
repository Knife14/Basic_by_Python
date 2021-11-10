"""
title: 矩阵置零
writer: 山客
date: 2021.3.21
example:
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)  # 行
        n = len(matrix[0])  # 列
        add_0 = []  # 0 的位置
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    add_0.append([i, j])
        for i in range(len(add_0)):
            for j in range(n):
                # 整行置零
                matrix[add_0[i][0]][j] = 0
            for j in range(m):
                # 整列置零
                matrix[j][add_0[i][1]] = 0
