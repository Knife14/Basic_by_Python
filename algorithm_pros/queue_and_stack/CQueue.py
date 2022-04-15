"""
title：用两个栈实现队列
writer：山客
date：2021.3.30
example：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
"""


class CQueue:

    def __init__(self):
        # A负责插入，B负责删除
        self.Astack = []
        self.Bstack = []

    def appendTail(self, value: int) -> None:
        # 从尾部添加，直接append即可
        self.Astack.append(value)

    def deleteHead(self) -> int:
        # 队列为空，返回-1
        if not self.Astack and not self.Bstack:
            return -1
        
        # 如果此时B栈已经有元素，则直接删除 - 即多次插入、删除操作后的情况
        if self.Bstack:
            return self.Bstack.pop()

        while self.Astack:
            self.Bstack.append(self.Astack.pop())

        return self.Bstack.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()