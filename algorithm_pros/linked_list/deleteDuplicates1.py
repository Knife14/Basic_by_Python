"""
title: 删除排序链接中的重复元素
writer: 山客
date: 2021.3.26
example:
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

输入：head = [1,1,1,2,3]
输出：[2,3]
"""

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                # 保留重复项的第一项
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head