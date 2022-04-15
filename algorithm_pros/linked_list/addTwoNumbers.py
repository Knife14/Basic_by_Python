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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)  # 进位carry

            curr.next = curr = ListNode(val)

        return head.next

