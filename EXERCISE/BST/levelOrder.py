"""
title：从上到下打印二叉树（树的BFS）
writer：山客
date：2021.4.12
key：双端队列 / 先序遍历
example：
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回：
[3,9,20,15,7]
"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderbyDeque(self, root: TreeNode) -> list:

        res = []

        if not root:
            return res

        # 引入双端队列
        queue = collections.deque()
        queue.append(root)

        while queue:
            # pop出队列中的头元素
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

    def levelOrderbyDFS(self, root):
        # write code here
        res = []

        def dfs_Preorder(root, level: int):
            if not root:
                return None

            if level >= len(res):
                res.append([])
            res[level].append(root.val)

            dfs_Preorder(root.left, level + 1)
            dfs_Preorder(root.right, level + 1)

        dfs_Preorder(root, 0)
        return res
