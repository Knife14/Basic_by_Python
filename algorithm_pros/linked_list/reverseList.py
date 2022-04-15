"""
title：反转链表
writer：山客
date：2021.4.8
key：双指针
example：
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
tips：
①迭代
②递归
③错误示范：pre, cur = cur, cur.next 只返回最末端节点，前面的节点被丢弃
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None

        # 迭代
        # pre->cur , cur -> cur.next
        # 赋值替换的顺序一定要注意！
        # 结束循环的条件是，cur.next == NULL
        while cur:
            nxt = cur.next
            
            cur.next = pre
            pre = cur
            cur = nxt

        return pre
