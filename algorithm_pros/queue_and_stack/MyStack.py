"""
title：用两个队列实现栈
writer：山客
date：2021.8.27
example：
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]
解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
tips:
① python一般队列都直接用deque（双向队列），所以用python做这条题没什么意义
② 普通队列先进先出
"""

from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Aqueue = deque()  # 负责插入
        self.Bqueue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.Aqueue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.Aqueue:
            self.Bqueue.append(self.Aqueue.popleft())

        return self.Bqueue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.Aqueue:
            self.Bqueue.append(self.Aqueue.popleft())

        return self.Bqueue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.Aqueue and not self.Bqueue:
            return True

        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
