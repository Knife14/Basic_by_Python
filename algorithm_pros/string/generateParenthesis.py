"""
title: 括号生成
writer: knife14
date: 2023.1.29
key: 递归
example:
输入: n = 3
输出: ["((()))","(()())","(())()","()(())","()()()"]
tips: 
1. 括号生成时，一定存在一对括号(a)b这种情况，a、b为剩余括号对的序列情况
"""

class Solution:
    # 暴力递归
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        # 生成所有可能，但不一定合法
        def generate_all(A):
            if len(A) == 2 * n:
                if isVaild(A):
                    res.append(''.join(A))
            else:
                A.append('(')
                generate_all(A)
                A.pop()
                A.append(')')
                generate_all(A)
                A.pop()
        
        # 判断括号闭合合法
        def isVaild(A):
            pair_num = 0
            for curr in A:
                if curr == '(':
                    pair_num += 1
                else:
                    pair_num -= 1
                if pair_num < 0:  # 提前结束
                    return False
            return pair_num == 0
        
        tmp = []
        generate_all(tmp)
        return res

    # 按括号序列的长度递归
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        
        res = []
        # ({left}){right}
        # i: 0, 1, ..., n - 1 除去必须有的一对，遍历剩下的对数
        # 先遍历left，right剩余对数即为 n - 1 - i
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    res.append('({}){}'.format(left, right))
        
        return res

a = Solution()
n = 2
print(a.generateParenthesis(n))
