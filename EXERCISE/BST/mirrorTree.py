"""
title：树的镜像
writer：山客
date：2021.4.9
key：递归
example：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode):

        if not root:
            return

        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)

        return root
