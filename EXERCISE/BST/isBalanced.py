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

# 先序遍历 + 判断深度：需要注意平衡二叉树的定义，是任一节点的左右子树高度差都在1或1以内才算成立
# 时间复杂度：O（NlogN） 空间复杂度：O（N）
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right)

    def depth(self, curr: TreeNode):
        if not curr:
            return 0
        
        return max(self.depth(curr.left), self.depth(curr.right)) + 1
