"""
title: 排序链表
writer: m14
date: 2024.4.9
key：归并排序
example:
输入：head = [4,2,1,3]
输出：[1,2,3,4]
说明：利用快慢指针二分链表直到每个链表只有一个节点，然后进行排序
thinking：
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.divide_merge(head)

    def divide_merge(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head_r = slow.next
        slow.next = None

        _L = self.divide_merge(head)
        _R = self.divide_merge(head_r)

        return self.merge_list(_L, _R)

    def merge_list(self, l: ListNode, r: ListNode) -> ListNode:
        dummy = ListNode()

        curr = dummy
        while l and r:
            print(l, r)
            if l.val > r.val:
                curr.next = r
                r = r.next
            else:
                curr.next = l
                l = l.next
            curr = curr.next
            
        if l:
            curr.next = l
        if r:
            curr.next = r

        return dummy.next
    

if __name__ == "__main__":
    a1 = ListNode(4)
    a2 = ListNode(1)
    a3 = ListNode(2)
    a4 = ListNode(3)
    
    a1.next = a2
    a2.next = a3
    a3.next = a4
    
    s = Solution()
    s.sortList(a1)
