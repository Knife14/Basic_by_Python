"""
title：从上到下打印二叉树②（树的BFS）
writer：山客
date：2021.4.12
example：
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回：
[
  [3],
  [9,20],
  [15,7]
]
"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        res = []

        if not root:
            return res

        # 引入双端队列
        queue = collections.deque()
        queue.append(root)

        while queue:
            # 重置每层temp
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)

        return res