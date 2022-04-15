"""
title：删除链表的倒数第n个节点
writer：山客
date：2021.8.30
key：双指针
example：
输入：
给定一个链表: 1->2->3->4->5, 和 k = 2.
输出：
返回链表 1->2->3->5
tips：
① 初解是先遍历链表长度l，再l + 1 - k择出所需节点
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self, head, n):
        # write code here
        times = head  # 用以计数倒数 n 个
        for _ in range(n):
            times = times.next
        if not times:
            return head.next

        curr = head
        while times.next:
            times = times.next
            curr = curr.next
        curr.next = curr.next.next

        return head
