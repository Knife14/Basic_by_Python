"""
title: 组合总和
writer: knife14
date: 2023.1.30
key: 回溯
example:
输入: candidates = [2,3,6,7], target = 7
输出: [[2,2,3],[7]]
tips: 
1. 因为序列中数值不重复，但同一数值可以重复使用，所以选择回溯
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def dfs_sum(num_path, begin, candidates, target):
            if target == 0:
                res.append(num_path)
                return 
            # 简单的剪枝
            elif target < 0:
                return 
            
            for index in range(begin, len(candidates)):
                dfs_sum(num_path + [candidates[index]], 
                        index, candidates, target - candidates[index])
     
        candidates.sort()
        dfs_sum([], 0, candidates, target)        
        return res

a = Solution()
n = [2,3,6,7]
print(a.combinationSum(n, 7))
