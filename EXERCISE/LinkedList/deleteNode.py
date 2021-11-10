"""
title: 删除链表中的节点
writer: 山客
date: 2021.4.6
example:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            # 删除头节点
            return head.next

        pre, cur = head, head.next
        while cur and cur.val != val:
            # 遍历节点，直到遍历到cur.val == val为止
            pre, cur = cur, cur.next

        if cur and cur.val == val:
            # 删除符合 cur.val == val 的cur节点
            pre.next = cur.next

        return head