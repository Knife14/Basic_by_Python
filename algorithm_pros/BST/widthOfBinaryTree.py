"""
title: 二叉树的最大宽度
writer: 山客
date: 2021.8.26
Key：DFS
problem：
输入:
           1
         /   \
        3     2
       / \     \
      5   3     9
输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
tips：
① 记录深度和位置，才好处理数据
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        left = {}
        def dfs(node, depth=0, pos=0):
            if node:
                left.setdefault(depth, pos)  # 记录第一个到达下一层深度的节点位置
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
