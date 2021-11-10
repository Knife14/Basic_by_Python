"""
title: 二叉树的最近公共祖先
writer: 山客
date: 2021.7.29
key：先序遍历
example:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
tips：
① 返回节点还是返回节点数据有轻微差别
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestorReturnNode(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestorReturnNode(root.left, p, q)
        right = self.lowestCommonAncestorReturnNode(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        return root

    def lowestCommonAncestorReturnVal(self, root, o1, o2):
        # write code here
        def dfs_Preorder(root, o1, o2):
            if not root or root.val == o1 or root.val == o2:
                return root

            left = dfs_Preorder(root.left, o1, o2)
            right = dfs_Preorder(root.right, o1, o2)

            # 如果一个在左，一个在右，则返回根节点
            if left and right:
                return root
            # 如果都在右，返回右节点
            if not left:
                return right
            # 如果都在左，返回左节点
            if not right:
                return left

        res = dfs_Preorder(root, o1, o2)
        return res.val
