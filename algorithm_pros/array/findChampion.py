"""
title: 找到冠军1
writer: m14
date: 2024.4.16
key：
example:
输入：grid = [[0,1],[0,0]]
输出：0
解释：比赛中有两支队伍。
grid[0][1] == 1 表示 0 队比 1 队强。所以 0 队是冠军。
thinking：
"""



class Solution:
    def findChampion_self(self, grid: List[List[int]]) -> int:
        cnt = [0] * len(grid)

        for idx, rels in enumerate(grid):
            for rel in rels:
                if rel:
                    cnt[idx] += 1

        return cnt.index(max(cnt))
    
    def findChampion_advanced(self, grid: List[List[int]]) -> int:
        for idx, rels in enumerate(grid):
            if sum(rels) == len(grid) - 1:
                return idx
