"""
title：包含min函数的栈
writer：山客
date：2021.4.11
example：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
tips：
① 数组下标 -1 即为 n - 1
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 栈A的最小元素始终对应栈B的栈顶元素
        self.A = []  # 正常栈
        self.B = []  # 存min值栈

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
