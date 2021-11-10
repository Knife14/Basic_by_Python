"""
title：二叉树中和为某一值的路径
writer：山客
date：2021.4.13
example：
给定如下二叉树，以及目标和 target = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list:
        res, path = [], []

        def sum(cur: TreeNode, target: int):
            # BST - 先序遍历
            if not cur:
                return

            path.append(cur.val)
            target -= cur.val
            if target == 0 and not cur.left and not cur.right:
                res.append(list(path))

            # 递归
            sum(cur.left, target)
            sum(cur.right, target)

            # 回溯 - 分别对左右子树进行再次检索
            # 清空path
            path.pop()

        sum(root, target)

        return res
