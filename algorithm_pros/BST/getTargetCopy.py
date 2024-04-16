"""
title: 找出克隆二叉树中的相同节点
writer: m14
date: 2024.4.16
key：递归
example:
输入: tree = [7,4,3,null,null,6,19], target = 3
输出: 3
解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
thinking：
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        
        if original == target:
            return cloned
        
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left
        
        right = self.getTargetCopy(original.right, cloned.right, target)
        if right:
            return right
