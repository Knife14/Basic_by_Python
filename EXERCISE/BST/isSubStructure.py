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

        def recur(a, b):
            if not b:
                # b 子树已经遍历完了
                return True

            if not a or a.val != b.val:
                # 正常判断是不是子树
                return False

            return (a.left, b.left) and (a.right, b.right)

        # 特例处理，A为空或B为空的时候，直接返回false
        # 正常三种情况：
        # ① B是否以A根节点的子树
        # ② B是否A的左子树
        # ③ B是否A的右子树
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
