"""
title: 删除排序链接中的重复元素2
writer: 山客
date: 2021.3.25
example:
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

输入：head = [1,1,1,2,3]
输出：[2,3]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pHead = ListNode(0, head)
        curr = pHead

        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                # 临时存储重复的值，记为x
                x = curr.next.val
                while curr.next and curr.next.val == x:
                    # 处理了大于等于3个重复项的最末项
                    # 只要curr.next.val == x，就会被下一项取代
                    # 直到curr.next.val != x
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return pHead.next