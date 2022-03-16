"""
title：栈的压入、弹出序列
writer：山客
date：2021.4.11
example：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出
"""


class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        stack = []
        n = 0

        for i in pushed:
            stack.append(i)
            
            # 防止越界： stack 可能是空的
            while stack and stack[-1] == popped[n]:
                stack.pop()
                n += 1

        if n == len(popped):
            return True
        
        return False
