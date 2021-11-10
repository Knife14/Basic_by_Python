"""
title: 复制带随机指针的链表
writer: 山客
date: 2021.3.24
example:
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:

    def __init__(self):
        self.visitHash = {}

    def copyRandomList(self, head):
        # 回溯

        # 链表为空
        if head == None:
            return None

        # 结点已访问过，则不创建新结点，直接return，防止成为死循环   
        if head in self.visitHash:
            return self.visitHash[head]

        # 之前没访问过该结点，则要创建一个新的节点，并且加入到已访问的字典中
        node = Node(head.val)
        self.visitHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
