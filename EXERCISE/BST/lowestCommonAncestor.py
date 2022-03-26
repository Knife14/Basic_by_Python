"""
title: 二叉搜索树的最近公共祖先
writer: 山客
date: 2021.7.29
example:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 一共有四种情况：都在左 / 右子树里，都不在，分别在左右子树
# 空间复杂度：O（N）    时间复杂度：O（N）
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and right:
            # must be not in left, so return right
            return right
        elif not right and left :
            # must be not in right, so return left
            return left
        elif left and right:
            # if all in, it makes sure the father node is the root 
            return root
        else:
            # if all not in, it makes sure there is not the father node
            return 
