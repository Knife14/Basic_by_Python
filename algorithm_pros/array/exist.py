"""
title: 矩阵的路径
writer: 山客
date: 2021.4.3
key：深度优先搜索（dfs）、剪枝
example:
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
thinking：
①已经检索选中的元素，不能再次选中，要返回false
"""


class Solution:
    def exist(self, board: list, word: str) -> bool:

        m, n = len(board), len(board[0])
        visited = set()

        def DFS(i, j, k) -> bool:

            if not 0 <= i < m \
                    or not 0 <= j < n \
                    or board[i][j] != word[k]:
                # 越界 or 不匹配，board[i][j] != word[k] 用于找到word中首个匹配元素
                return False

            if k == len(word) - 1:
                # 完成匹配
                return True

            # 将匹配元素设置成空字符，代表已经访问过，可避免后续检索时返回到该位，违反题目要求
            board[i][j] = ''

            # 对匹配元素的上下左右进行dfs检索，type(res) = bool
            res = DFS(i + 1, j, k + 1) or DFS(i, j + 1, k + 1) or DFS(i - 1, j, k + 1) or DFS(i, j - 1, k + 1)

            # 将空字符设置回原来的字符
            board[i][j] = word[k]

            return res

        for i in range(m):
            for j in range(n):
                # 不能写成 return DFS(i, j, 0)
                # 这样会每次循环都返回一个值，这是不对的
                if DFS(i, j, 0):
                    return True

        return False
