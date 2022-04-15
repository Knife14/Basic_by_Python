"""
title：对称的二叉树
writer：山客
date：2021.4.9
key：递归
example：
输入：root = [1,2,2,3,4,4,3]
输出：true

输入：root = [1,2,2,null,3,null,3]
输出：false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            # 树是空的，返回true
            return True

        def recur(a, b):
            if not a and not b:
                # 遍历到空为止，依然是true，则true
                return True
            if not a or not b or a.val != b.val:
                # 正常判断，左左等于右右，左右等于右左
                return False

            return recur(a.left, b.right) and recur(a.right, b.left)

        return recur(root.left, root.right)