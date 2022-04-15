"""
title：航海探险
writer：山客
date：2021.8.21
key：
example：
输入：
[[1,1,1,1,0],[0,1,0,1,0],[1,1,2,1,1],[0,2,0,0,1]]
输出：
7
tips：
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 计算最小航行费用
# @param input int整型二维数组 二维网格
# @return int整型
#
mod = 1_000_000_007

class Solution:
    def minSailCost(self , input ):
        # write code here
        def BFS(cmap: list):
            n, m = len(cmap), len(cmap[0])  # 行， 列
            cnt = [[0] * (m + 1) for _ in range(n + 1)]

            for i in range(1, m + 1):
                cnt[0][i] += cnt[0][i - 1] + cmap[0][i - 1]
            for j in range(1, n + 1):
                cnt[j][0] += cnt[j - 1][0] + cmap[j - 1][0]

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    cnt[i][j] += min(
                            cnt[i][j - 1] + cmap[i - 1][j - 1],
                            cnt[i - 1][j] + cmap[i - 1][j - 1]
                    )

            if cnt[-1][-1] >= mod:
                return -1
            else:
                return cnt[-1][-1]

        cmap = [[0] * len(input[0]) for _ in range(len(input))]
        for i in range(len(input)):
            for j in range(len(input[0])):
                if input[i][j] == 0:
                    cmap[i][j] = 2
                elif input[i][j] == 1:
                    cmap[i][j] = 1
                elif input[i][j] == 2:
                    cmap[i][j] = mod
        cmap[0][0] = 0
        res = BFS(cmap)

        return res


if __name__ == '__main__':
    data = [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 1, 2, 1, 1], [0, 2, 0, 0, 1]]

    s = Solution()
    res = s.minSailCost(data)
    print(res)
