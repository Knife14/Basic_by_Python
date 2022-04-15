"""
title: 森林中的兔子
writer: 山客
date: 2021.4.5
key：贪心算法
problem：
森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。
我们将这些回答放在 answers 数组里。返回森林中兔子的最少数量。
example:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11
"""


class Solution:
    def numRabbits(self, answers: list) -> int:
        res = 0
        colors = {}

        if not answers:
            return 0

        for i in answers:
            if i not in colors.keys():
                colors[i] = 1
            else:
                colors[i] += 1

        for k, v in colors.items():
            # 一般地，如果有x只兔子回答y，则至少有（x / y+1）种不同的颜色，且兔子数为y+1只
            res += (v + int(k)) // (int(k) + 1) * (int(k) + 1)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numRabbits([1,0,1,0,0]))