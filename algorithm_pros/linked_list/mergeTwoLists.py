"""
title：合并两个排序的链表
writer：山客
date：2021.4.9
key：迭代
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
        head = ListNode(0)
        
        curr = head
        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            # 这一步很重要
            # 把当前节点移动到新增的节点，以便链表的延长
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return head.next
