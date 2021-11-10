"""
title：链表中倒数第k个节点
writer：山客
date：2021.4.9
key：双指针
example：
输入：
给定一个链表: 1->2->3->4->5, 和 k = 2.
输出：
返回链表 4->5
tips：
①初解是先遍历链表长度l，再l + 1 - k择出所需节点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int):
        former, latter = head, head

        '''
        双指针：
        former指针先移动k次，剩下l + 1 - k次
        再让latter从头顶点移动l + 1 - k次，即可实现所需效果
        '''

        for i in range(k):
            if not former:
                return 0
            former = former.next

        while former:
            former, latter = former.next, latter.next

        return latter
