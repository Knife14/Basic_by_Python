"""
title：从上到下打印二叉树③（树的BFS）
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
  [20,9],
  [15,7]
]
tips：
① 奇数层打印头部，偶数层先打印尾部
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
            temp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2:
                    # 偶数层，从左开始打印 - 由于数组下标和逻辑下标相差1，所以这里的表示方式是不同的。
                    temp.appendleft(node.val)
                else:
                    # 奇数层，从右开始打印 - 由于数组下标和逻辑下标相差1，所以这里的表示方式是不同的。
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(temp))

        return res