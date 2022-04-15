"""
title: 二叉搜索树节点最小距离
writer: 山客
date: 2021.4.13
problem：
给一个二叉搜索树的根节点 root ，返回树中任意两不同节点值之间的最小差值
example:
输入：root = [4,2,6,1,3]
输出：1

输入：root = [1,0,48,null,null,12,49]
输出：1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        self.vals = []
        self.inOrder(root)

        return min([self.vals[i + 1] - self.vals[i] for i in range(len(self.vals) - 1)])

    def inOrder(self, root: TreeNode):
        # 由于是求最小值，所以使用中序遍历
        # 中序遍历出来的vals数组将会呈升序排序
        if not root:
            return
        self.vals.append(root.val)
        self.inOrder(root.left)
        self.inOrder(root.right)
