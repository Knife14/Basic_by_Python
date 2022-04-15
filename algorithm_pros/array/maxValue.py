"""
title: 礼物的最大价值
writer: 山客
date: 2021.7.29
example:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
"""


class Solution:
    def maxValue(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])

        return grid[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.maxValue(
        [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
    ))
