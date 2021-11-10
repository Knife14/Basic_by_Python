"""
title: 逆波兰表达式
writer: 山客
date: 2021.3.20
example:
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
"""

import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        temp_result = []
        for i in tokens:
            if i not in '+-/*':
                temp_result.append(int(i))
            else:
                # pop出末位（最新加入位）
                num1 = temp_result.pop()
                num2 = temp_result.pop()
                result = self.do_math(i, num2, num1)
                temp_result.append(int(result))
        return int(temp_result.pop())

    def do_math(self,method, x, y):
        if method == '+':
            return x + y
        elif method == '-':
            return x - y
        elif method == '*':
            return x * y
        elif method == '/':
            # 整数除法只保留整数部分
            if x < 0 and y < 0:
                return x // y
            elif x < 0 or y < 0:
                return (math.ceil(x/y))
            else:
                return x // y

