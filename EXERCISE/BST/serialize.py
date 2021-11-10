"""
title：序列化二叉树
writer：山客
date：2021.4.13
example：
输入：
      1
    /   \
   2     3
        /  \
       4    5
输出：
[1,2,3,null,null,4,5] -> str
"""

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        BST -> list -> str
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"

        queue = collections.deque()
        queue.append(root)

        res = []

        while queue:
            node = queue.popleft()
            if node:
                # 先序遍历
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                # 空的append “null”
                res.append("null")

        return '[' + ','.join(res) + ']'

    def deserialize(self, data: int):
        """
        Decodes your encoded data to tree.
        str -> list -> BST
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return

        vals = data[1: -1].split(',')
        root = TreeNode(int(vals[0]))
        index = 1

        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            # 左节点
            if vals[index] != "null":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            # 右结点
            index += 1
            if vals[index] != "null":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            # 左子树到右子树 / 下一层
            index += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
