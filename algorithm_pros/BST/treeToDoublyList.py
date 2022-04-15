"""
title：二叉搜索树与双向链表
writer：山客
date：2021.4.13
problem：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
example：
输入：
      4
    /   \
   2     5
 /  \
1    3
输出：
双向循环链表：5 <- 1 -><- 2 -><- 3 -><- 4 -><- 5 -> 1
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node'):
        # 头结点 - 头结点的前驱结点就是cur的前一个结点， 用于构建循环链表
        self.head = root
        # 前驱结点 - 前驱结点后面跟着的结点就是cur， 用于构建双向链表
        self.pre = None

        # 中序遍历，构建双向链表
        def dfs_middle(cur: 'Node'):
            if not cur:
                return

            dfs_middle(cur.left)
            # 执行操作
            if self.pre:
                # 双向链表
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur

            dfs_middle(cur.right)

        if not root:
            return

        dfs_middle(root)

        # 循环链表
        self.head.left, self.pre.right = self.pre, self.head

        return self.head
