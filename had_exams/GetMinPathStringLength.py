"""
title：最短路径字符串
writer：山客
date：2021.8.10
key：动态规划
example：
输入：
3,4,"wh|js|bg|/jsbg|b|rj|yx/rjyxgs|g||gs/"
输出：
8
tips：
① 其他寻路算法应该也可以解答
"""


#
# 返回最短路径组成的字符串的长度
# @param m int整型 表格行数
# @param n int整型 表格列数
# @param strTableContent string字符串 表格字符串表示
# @return int整型
#
class Solution:
    def GetMinPathStringLength(self, m: int, n: int, strTableContent: str):

        # 处理字符串
        def StrToList():
            map = [[] for _ in range(m)]
            line = column = 0  # 当前行，当前列
            low = high = 0  # 双指针

            for i in range(len(strTableContent)):
                if strTableContent[i] == '|':
                    map[line].append(strTableContent[low: high])
                    low = high = i + 1
                elif strTableContent[i] == '/':
                    map[line].append(strTableContent[low: high])
                    low = high = i + 1
                    line += 1
                else:
                    high += 1

            return map

        # 寻找路径
        def FindPath(map: list):
            data = [[] for _ in range(m)]

            for i in range(len(map)):
                for j in range(len(map[0])):
                    data[i].append(len(map[i][j]))
            # print(data)

            # 动态规划
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = data[0][0]
            for i in range(1, m):
                dp[i][0] = data[i][0] + dp[i - 1][0]
            for j in range(1, n):
                dp[0][j] = data[0][j] + dp[0][j - 1]
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + data[i][j]
            # print(dp)

            return dp[m - 1][n - 1]

        map = StrToList()  # 处理字符串
        return FindPath(map)


if __name__ == '__main__':
    m, n, strTableCont = input().split()
    s = Solution()
    print(s.GetMinPathStringLength(int(m), int(n), strTableCont))
