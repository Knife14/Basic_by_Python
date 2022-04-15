"""
title：合并两个排序的链表
writer：山客
date：2021.4.9
key：双指针
example：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # dum 为伪造的头节点
        cur = dum = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next

        # 两个链表还有剩下的部分节点
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        return dum.next
