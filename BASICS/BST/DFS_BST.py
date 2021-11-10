"""
title：二叉搜索树的三种遍历
writer：山客
date：2021.4.13
example：
      A
    /   \
   B     C
 /  \   /
 D   E F
tips：
① 先序遍历： 根节点->左节点->右节点  A->B->D->E->C->F
② 中序遍历： 左节点->根节点->右节点  D->B->E->A->F->C
③ 后序遍历： 左节点->右节点->根节点  D->E->B->F->C->A
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs_Preorder(self, root):
        # 先序遍历
        if not root:
            return

        # 若有操作块，则在此处添加

        self.dfs_Preorder(root.left)
        self.dfs_Preorder(root.right)

    def dfs_Middle(self, root):
        # 中序遍历
        if not root:
            return

        self.dfs_Middle(root.left)

        # 若有操作块，则在此处添加

        self.dfs_Middle(root.right)

    def dfs_Postorder(self, root):
        # 后序遍历
        if not root:
            return

        self.dfs_Postorder(root.left)
        self.dfs_Postorder(root.right)

        # 若有操作块，则在此处添加
