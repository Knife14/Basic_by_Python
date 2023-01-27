"""
title: 两数相加
writer: 山客
date: 2021.3.23
example:
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
     # 思考过程
     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        new_node = ListNode()
        res.next = new_node
        car = 0
        while l1 and l2:
            if new_node.next:
                new_node = new_node.next
            new_node.val = (l1.val + l2.val + car) % 10
            car = 1 if l1.val + l2.val + car >= 10 else 0

            l1 = l1.next
            l2 = l2.next
            if l1 or l2:
                new_node.next = ListNode()
        if l1:
            new_node.next = l1
        if l2:
            new_node.next = l2
        while new_node.next:
            new_node = new_node.next
            tmp = new_node.val
            new_node.val = (tmp + car) % 10
            car = 1 if (tmp + car) >= 10 else 0
        if car == 1:
            new_node.next = ListNode(1)

        return res.next
     
     # 简洁写法
     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)  # 除商carry，余数val
            """
            curr.next = ListNode(val)
            curr = curr.next
            python 同时赋多个值时，先处理左边的。即a=b=[1]时，先处理a=[1]，再处理b=[1]
            """
            curr.next = curr = ListNode(val)

        return head.next

