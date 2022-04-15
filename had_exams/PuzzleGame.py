"""
title：拼图游戏
writer：山客
date：2021.9.18
key：
example：
输入：
3 3
1 2 4 8 6
2 0 5 1 7
3 4 0 0 8
4 5 0 3 1
5 0 0 4 2
6 7 1 9 0
7 0 2 6 0
8 1 3 0 9
9 6 8 0 0
输出：
5 4 3
2 1 8
7 6 9
tips：
"""

class Solution:
    def PuzzleGame(self, size: list, NOdict: dict) -> list:
        n, m = size[0], size[1]  # n 行 m 列
        res = [[0] * m for _ in range(n)]

        # 处理四角
        for k, v in NOdict.items():
            # 左上
            if v[0] == 0 and v[1] == 0:
                res[0][0] = k
            # 右上
            elif v[1] == 0 and v[2] == 0:
                res[0][m - 1] = k
            # 左下
            elif v[0] == 0 and v[3] == 0:
                res[n - 1][0] = k
            # 右下
            elif v[2] == 0 and v[3] == 0:
                res[n - 1][m - 1] = k
            else:
                continue

        # 处理四边，左右 and 上下
        # 存储节点顺序为：左上右下
        for i in range(1, n - 1):
            res[i][0] = NOdict[res[i - 1][0]][3]
            res[i][m - 1] = NOdict[res[i - 1][m - 1]][3]
        for j in range(1, m - 1):
            res[0][j] = NOdict[res[0][j - 1]][2]
            res[n - 1][j] = NOdict[res[n - 1][j - 1]][2]

        # 处理中心区域
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                res[i][j] = NOdict[res[i - 1][j]][3]

        return res


if __name__ == '__main__':
    s = Solution()

    size = list(map(int, input().split()))
    NOdict = {}
    for _ in range(size[0] * size[1]):
        tmp = list(map(int, input().split()))
        NOdict[tmp[0]] = tmp[1:]

    ress = s.PuzzleGame(size, NOdict)
    for res in ress:
        for r in res:
            print(r, end=' ')
        print()
