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
    # 队列
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
                node = queue.popleft()  # 一定要从queue队列头取出节点
                if len(res) % 2:
                    temp.appendleft(node.val)
                else:
                    temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(temp))

        return res
    
    # 数组
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, queue = [], [root]
        line = 0

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)  # 一定要从数组头取出节点
                if line % 2 == 0:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
            line += 1

        return res
