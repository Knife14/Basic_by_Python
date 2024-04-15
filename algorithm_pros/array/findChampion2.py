"""
title: 找到冠军2
writer: m14
date: 2024.4.15
key：
example:
输入：n = 4, edges = [[0,2],[1,3],[1,2]]
输出：-1
解释：2 队比 0 队和 1 队弱。3 队比 1 队弱。但是 1 队和 0 队之间不存在强弱对比。所以答案是 -1 。
thinking：
"""


class Solution:
    def findChampion_basic(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return 0

        cham = []
        losed = []

        for w, l in edges:
            if w not in cham and w not in losed:
                cham.append(w)

            if l not in losed:
                losed.append(l)
            if l in cham:
                cham.remove(l)
            print(cham)

        return cham[0] if len(cham) == 1 and len(cham) + len(losed) == n else -1

    def findChampion_advanced(self, n: int, edges: List[List[int]]) -> int:
        res = [0] * n
        
        for _, losed in edges:
            res[losed] += 1
        
        return -1 if res.count(0) != 1 else res.index(0)
