"""
title: 从尾到头打印链表
writer: 山客
date: 2022.3.13
example:
输入：head = [1,3,2]
输出：[2,3,1]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 辅助栈概念： nums 即为辅助栈
class Solution:
    def reversePrint(self, head: 'ListNode'):
        nums = list()

        curr = head
        while curr:
            nums.append(curr.val)

            curr = curr.next
        
        return list(reversed(nums))  # nums[::-1]

      
if __name__ == '__main__':
	s = Solution()

	head = ListNode(1)
	next1 = ListNode(2)
	next2 = ListNode(3)
	head.next = next1
	next1.next = next2

	print(s.reversePrint(head))
