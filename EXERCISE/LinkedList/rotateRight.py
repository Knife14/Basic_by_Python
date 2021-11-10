"""
title：旋转链表
writer：山客
date：2021.3.27
example：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]
"""

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head

        while cur.next:
            cur = cur.next
            n += 1  # ListNode的长度

        # 若k是n的倍数，可视为没有旋转移动，返回原链表即可
        add = n - k % n
        if add == n:
            return head

        # 此时curr是链表的最后一位元素，curr.next = head构成闭环
        cur.next = head

        while add:
            # 循环add-1次
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None

        return ret