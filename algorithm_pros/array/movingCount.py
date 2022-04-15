"""
title: 机器人的运动范围
writer: 山客
date: 2021.4.3
key：
problem：
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
example:
输入：m = 2, n = 3, k = 1
输出：3

输入：m = 3, n = 1, k = 0
输出：1
tips：
① set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
② 还可使用广度搜索（BFS）等方法进行解答
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()

        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or (i,j) in visited or \
                (i % 10 + i // 10 + j % 10 + j // 10) > k:
                return 0
            visited.add((i, j))

            return 1 + dfs(i + 1, j, k) + dfs(i - 1, j, k) + dfs(i, j + 1, k) + dfs(i, j - 1, k)

        return dfs(0, 0, k)


if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(3, 2, 1))
