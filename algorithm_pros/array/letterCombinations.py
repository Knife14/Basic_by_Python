"""
title: 电话号码的字母组合
writer: knife14
date: 2023.1.29
key: 回溯
example:
输入: digits = "23"
输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
tips:
1. 
"""

class Solution:
    # 思考过程
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        res = []
        num_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        digits_list = list(digits)
        while digits_list:
            curr_letter = digits_list.pop(0)
            if not res:
                res.extend(num_letter_map[curr_letter])
            else:
                for _ in range(len(res)):
                    r = res.pop(0)
                    res.extend(r + l for l in num_letter_map[curr_letter])
        return res
    
    # 更简便的回溯写法
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: 
            return []

        num_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in num_letter_map[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1: ])

        res = []
        backtrack('', digits)
        return res

a = Solution()
digits = "23"
print(a.letterCombinations(digits))
