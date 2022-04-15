"""
title：钱老板刷怪
writer：山客
date：2021.9.18
key：
example：
输入：
3 3 1 1 2 2 3 3
输出：
3
tips：
① 可能超时了？？？ 14 / 15
"""

class Solution:
    def BrushBlame(self, N: int, COUNT: int, POST: list) -> int:
        # 技能A ： 横纵、正斜线
        # 技能B ： 正方形范围，边长为 2 * N + 1

        maxA = maxB = 0
        Blen = (2 * N + 1) / 2  # 以玩家坐标为中心，所以要折半

        # 选起点
        for currX, currY in POST:
            # 技能A
            # 行、列、左斜、右斜
            line = column = left = right = 0
            for x, y in POST:
                # 行
                if x == currX:
                    line += 1
                # 列
                if y == currY:
                    column += 1
                # 左斜
                if ((x - currX) <= 0 and (y - currY) >= 0 and (x - currX + y - currY) == 0) \
                        or ((x - currX) >= 0 and (y - currY) <= 0 and (x - currX + y - currY) == 0):
                    left += 1
                # 右斜
                if ((x - currX) >= 0 and (y - currY) >= 0 and (x - currX - y + currY) == 0) \
                        or ((x - currX) <= 0 and (y - currY) <= 0 and (x - currX - y + currY) == 0):
                    right += 1
            maxA = max(line, column, left, right)
            if maxA >= COUNT:
                return COUNT

            # 技能 B
            tmpB = 0
            for x, y in POST:
                if abs(x - currX) <= Blen and abs(y - currY) <= Blen:
                    tmpB += 1
            maxB = max(tmpB, maxB)
            if maxB >= COUNT:
                return COUNT

        return min(max(maxA, maxB), COUNT)


if __name__ == '__main__':
    data = list(map(int, input().split()))

    # 数据处理
    N = data[0]  # 技能 B 的正方形边长
    COUNT = data[1]  # 怪物总数
    POST = []
    for i in range(2, len(data) - 1, 2):
        POST.append((data[i], data[i + 1]))

    s = Solution()
    res = s.BrushBlame(N, COUNT, POST)
    print(res)
