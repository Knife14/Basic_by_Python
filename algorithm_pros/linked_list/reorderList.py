"""
title: 重排链表
writer: m14
date: 2024.4.9
key：反转链表，越界处理
example:
输入: head = [1,2,3,4,5]
输出: [1,5,2,4,3]
thinking：
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pre = ListNode()
        pre.next = head
        
        slow = fast = pre
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # to confirm the right half with the end node
        half = slow.next
        slow.next = None
        _r = self.reverseList(half)
        
        curr = head
        while _r:
            tmp = curr.next
            curr.next = _r
            _r = _r.next
            curr = curr.next
            curr.next = tmp
            curr = curr.next
    
    def reverseList(self, head: ListNode) -> ListNode:
        pre, curr = None, head
        
        while curr:
            tmp = curr.next
            curr.next = pre
            pre, curr = curr, tmp
            
        return pre


if __name__ == "__main__":
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(3)
    a4 = ListNode(4)
    
    a1.next = a2
    a2.next = a3
    a3.next = a4
    
    s = Solution()
    s.reorderList(a1)
    
    t = a1
    while t:
        print(t.val)
        t = t.next
