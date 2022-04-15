"""
title: 子集②
writer: 山客
date: 2021.3.31
Key：回溯法
example:
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

输入：nums = [0]
输出：[[],[0]]
"""


class Solution:

    def subsetsWithDup(self, nums: list) -> list:
        res = []

        nums.sort()

        self.dfs(nums, 0, res, [])

        return res

    def dfs(self, nums: list, index, res, path):
        if path not in res:
            # 每一条路径，每次循环都会append，则可以完成[[1],[1,2],[1,2,2]]效果
            res.append(path)

        for i in range(index, len(nums)):
            # 自动更新path = []，以达到[1],[2]结果
            if i > index and nums[i] == nums[i - 1]:
                # 重复元素只能选其一，故continue，无视该次for
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])
