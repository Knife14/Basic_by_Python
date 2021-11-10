"""
title: 笨阶乘
writer: 山客
date: 2021.4.1
example:
输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
thinking：
① * / + - 按规律添加
②乘除立即算，加减先入栈
③sum()函数对序列求和
"""


class Solution:
    def clumsy(self, N: int) -> int:

        op = 0  # 状态值，用于判断四则运算
        stack = [N]  # 栈保存的是具体数值，不保存运算符

        for i in range(N - 1, 0, -1):
            # 从N开始，每个数值元素逐渐递减
            # 乘除直接算，加减先入栈
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / i))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            op = (op + 1) % 4

        # 解决加减先入栈的因素
        return sum(stack)