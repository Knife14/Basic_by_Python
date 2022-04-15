"""
title：重建二叉树
writer：山客
date：2021.3.29
example：
给出：
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回：
    3
   / \
  9  20
    /  \
   15   7
thinking:
①递归：在递归的每一部分中，其实都只是找到了属于根节点的点，从而最终递归出一整棵树
②在中序遍历中定位到根节点，即可知左子树和右子树的节点数目（相对于根节点而言）
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归1
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) != len(inorder):
            return None
        elif not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])  # determine the root node
        
        # get the index of root in the inorder list
        pos = inorder.index(preorder[0])
        
        # get the preorder and the inorder of left tree
        left_perorder = preorder[1: pos + 1]
        left_inorder = inorder[:pos]
        # get the right
        right_perorder = preorder[pos + 1:]
        right_inorder = inorder[pos + 1:]

        # recursion
        left_stree = self.buildTree(left_perorder, left_inorder)
        right_stree = self.buildTree(right_perorder, right_inorder)

        # result
        root.left = left_stree
        root.right = right_stree
        return root
        
# 递归2
class Solution:
    def buildTree(self, preorder: list, inorder: list):

        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点，element数据，i为数据下标
        index = {element: i for i, element in enumerate(inorder)}
        """
        numerate()函数：
        用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
        同时列出数据下标和数据。
        """

        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None

            # 前序遍历中的第一个节点是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])

            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left

            # 递归地构造左子树，并连接到根节点
            """
            先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素
            对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            """
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree,
                                    inorder_left, inorder_root - 1)

            # 递归地构造右子树，并连接到根节点
            """
            先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素
            对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            """
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right,
                                     inorder_root + 1, inorder_right)
            return root

        return myBuildTree(0, n - 1, 0, n - 1)
