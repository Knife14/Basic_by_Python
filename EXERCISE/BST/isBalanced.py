"""
title：判断平衡二叉树
writer：山客
date：2021.4.18
key：先序遍历
example：
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

返回 true 。

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

返回 false 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return False

        deep = [0] * 2

        def count(root: TreeNode):

            n = 0

            if not root:
                return 0

            n += 1 + max(count(root.left), count(root.right))

            return n

        # 左右子树深度，0 - 左子树， 1 - 右子树
        # 平衡二叉树定义：左右子树深度不能大于1
        deep[0] = count(root.left)
        deep[1] = count(root.right)

        if abs(deep[0] - deep[1]) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            # 递归
            # 确保每个节点的左右子树都符合平衡二叉树定义
            return True
        else:
            return False
