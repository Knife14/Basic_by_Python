"""
title：从尾到头打印链表
writer：山客
date：2021.3.29
example：
输入：head = [1,3,2]
输出：[2,3,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list:

        vals = []
        res = []

        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        # print(vals)
        for i in range(len(vals) - 1, -1, -1):
            res.append(vals[i])
        # print(res)

        return res


if __name__ == '__main__':
    head = ListNode(1)
    l1 = ListNode(3)
    l2 = ListNode(2)
    head.next = l1
    l1.next = l2

    res = Solution()
    n = res.reversePrint(head)