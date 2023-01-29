"""
title: 有效的括号
writer: knife14
date: 2023.1.29
key: 正确顺序闭合 -> 辅助栈
example:
输入: s = "()[]{}"
输出: true
输入: s = "([)]"
输出: false
tips: 
"""

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            '(': ')',
            '[': ']',
            '{': '}',
            '?': '?'  # 这个对应关系，涉及到后面的stack.pop映射，算异常处理
        }
        
        stack = ['?']
        for c in s:
            if c in brackets_map:
                stack.append(c)
            elif c != brackets_map[stack.pop()]:
                return False
        
        return len(stack) == 1

a = Solution()
s = "]"
print(a.isValid(s))
