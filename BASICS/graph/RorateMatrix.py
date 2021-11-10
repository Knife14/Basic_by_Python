"""
title：旋转（顺时针）矩阵
writer：山客
date：2021.9.4
tips：
① 仅针对 n * n 矩阵
"""


def RorateMatrix(matrix: list):
    n = len(matrix)

    # 对角线（左上右下）翻转
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 行翻转
    for i in range(n):
        matrix[i].reverse()

    return matrix
