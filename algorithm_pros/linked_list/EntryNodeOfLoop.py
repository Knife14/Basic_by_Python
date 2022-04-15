"""
title: 链表中环的入口结点
writer: 山客
date: 2021.8.30
key：浪漫相遇
example:
输入：{1,2},{3,4,5}
返回值：3
说明：返回环形链表入口节点，我们后台会打印该环形链表入口节点，即3
thinking：
"""


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None

        low = pHead.next
        fast = pHead.next.next

        # 先确认有链表环
        while fast and fast != low:
            if fast.next:
                fast = fast.next.next
            low = low.next

        # 确认有环，后再找到环入口
        if fast is not None:
            while pHead != low:
                low = low.next
                pHead = pHead.next
            return low
        else:
            return None
