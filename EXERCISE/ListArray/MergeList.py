"""
title: 合并区间
writer: 山客
date: 2021.11.9
key：厘清区间重合的逻辑
example:
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
"""


class Solution:
    def merge(self, intervals: list) -> list:
        res = list()

        sorted_inters = sorted(intervals, key=lambda x: x[0])

        for inter in sorted_inters:
            # 保证前一区间的终点与下一区间的起点不重合
            if not res or inter[0] > res[-1][1]:
                res.append(inter)
            # 否则，适当比较以扩大当前区间
            else:
                res[-1][-1] = max(res[-1][-1], inter[-1])

        return res
