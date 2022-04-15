"""
title: 二叉树的深度
writer: 山客
date: 2021.4.18
example:
输入:
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7

返回它的最大深度 3 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 深度搜索 + 先序遍历
# 时间复杂度：O（N） 空间复杂度：O（N）
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr: TreeNode, t: int):
            if curr:
                t += 1
            else:
                self.res = max(t, self.res)
                return 
            
            dfs(curr.left, t)
            dfs(curr.right, t)

        dfs(root, 0)

        return self.res
