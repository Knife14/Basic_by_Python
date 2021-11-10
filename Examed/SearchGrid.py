"""
title：字符网格搜索单词
writer：山客
date：2021.9.6
key：DFS（深度优先搜索）
example：
输入：
[[a,b],[a,b]],"aba"
输出：
false
tips：
① 解决开始节点
② 超时 9 / 10
"""


class Solution:
    def exist(self, board, word):
        def DFS(board: list, x: int, y: int, word: str, index: int):
            # 越界
            if (0 > x or x >= len(board))\
                    or (0 > y or y >= len(board[0])) \
                    or word[index] != board[x][y]:
                return False

            # 遍历完 word 即返回 True
            if index == len(word) - 1:
                return True

            board[x][y] = '/'

            # 上下左右四个方向
            # 深度搜索：即在当前基础上，已经遍历过的点就被之后忽略
            res = DFS(board, x + 1, y, word, index + 1) \
                  or DFS(board, x - 1, y, word, index + 1) \
                  or DFS(board, x, y + 1, word, index + 1) \
                  or DFS(board, x, y - 1, word, index + 1)

            board[x][y] = word[index]

            return res

        if len(word) == 1 and word in board:
            return True

        begins = []
        # 两轮遍历以解决有多种开头的可能
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    begins.append((i, j))

        # 分开处理，提高效率，防止超时
        for begin in begins:
            if DFS(board, begin[0], begin[1], word, 0):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.exist([['a', 'b'], ['a', 'b']], "aba"))
