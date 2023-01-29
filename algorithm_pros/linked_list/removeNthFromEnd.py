"""
title：删除链表的倒数第n个节点
writer：山客
date：2021.8.30
key：快慢指针，栈
example：
输入：
给定一个链表: 1->2->3->4->5, 和 k = 2.
输出：
返回链表 1->2->3->5
tips：
① 利用两条链表（长度相差n）遍历选出完整链表应该被删除的节点
② 快慢指针，原理跟1相近
③ 栈，利用先进后出的原理，可以在出栈的时候按倒序找到想要的第n个节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param head ListNode类
# @param n int整型
# @return ListNode类
#
class Solution:
    # 遍历链表
    def removeNthFromEnd(self, head, n):
        # write code here
        times = head  # 用以计数倒数 n 个
        for _ in range(n):
            times = times.next
        if not times:
            return head.next
        
        # 两条链表长度相差n，遍历短的到尽头，那长的就会正好遍历到要删除节点的前一个位置（因为while times.next）
        curr = head
        while times.next:
            times = times.next
            curr = curr.next
        curr.next = curr.next.next

        return head
    
    # 快慢指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = ListNode(0, head)
        first, second = head, curr  # 快慢指针，相隔 n
        for _ in range(n):
            first = first.next
        
        # 当first为空时，second就在需要删除节点的前一位
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return curr.next
    
    # 栈，先进后出
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        stack = []
        origin = curr = ListNode(0, head)  # 确保 n 与 链表长度相同时，不会产生越界并返回正确的空结果
        while curr:
            stack.append(curr)
            curr = curr.next
        
        for _ in range(n):
            stack.pop()
        prev_node = stack[-1]
        prev_node.next = prev_node.next.next
        
        return origin.next
