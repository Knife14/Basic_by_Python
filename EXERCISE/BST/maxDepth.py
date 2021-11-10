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


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(root: TreeNode):
            if not root:
                return 0

            return 1 + max(dfs(root.left), dfs(root.right))

        return dfs(root)