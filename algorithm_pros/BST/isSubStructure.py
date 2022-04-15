"""
title：树的子结构
writer：山客
date：2021.4.9
key：递归
example：
输入：A = [1,2,3], B = [3,1]
输出：false

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False

        def dfs(a: TreeNode, b: TreeNode):
            if not b:
                return True
            
            # 防止越界
            if not a:
                return False

            if a.val != b.val:
                return False

            return dfs(a.left, b.left) and dfs(a.right, b.right)
        
        # 正常三种情况：
        # ① B是否以A根节点的子树
        # ② B是否A的左子树
        # ③ B是否A的右子树
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
