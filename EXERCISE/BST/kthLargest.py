"""
title: 二叉搜索树的第k大节点
writer: 山客
date: 2021.4.18
example:
输入:
root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        if not root:
            return 0

        vals = []

        def dfs(root: TreeNode):

            if not root:
                return

            vals.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        vals = sorted(vals)

        return vals[len(vals) - k + 1]