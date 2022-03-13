"""
title：二维数组中的查找
writer：山客
date：2021.3.29
example：
输入：现有矩阵如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
"""

# 简单做法： 遍历n行，根据递增原则逐列判断，若出现遍历值小于但不等于目标值的情况，则跳过该行
# 时间复杂度： O（N + MlogN） 空间复杂度： O（1）
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m - 1, -1, -1):
                if target > matrix[i][j]:
                    break
                elif target == matrix[i][j]:
                    return True


        return False

# 标志数： 利用二叉树左小右大的定义，从矩阵左下角开始遍历判断，移动的方向只有上或者右
# 时间复杂度： O（M + N）  空间复杂度： O（1）
class Solution:
    def findNumberIn2DArray(self, matrix: list, target: int) -> bool:

        if not matrix:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target < matrix[i][j]:
                    continue
                if target == matrix[i][j]:
                    return True

        return False
