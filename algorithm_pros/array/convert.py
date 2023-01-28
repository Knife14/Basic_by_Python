"""
title: Z字形变换
writer: knife14
date: 2023.1.28
key: 
example:
输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
解释: 
P   A   H   N
A P L S I I G
Y   I   R
tips:
1. 矩阵的列数可以进行内存优化
2. Leetcode上还有别的解法，可以参考
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2 or len(s) <= 1:
            return s
        
        s_len, index = len(s), 0
        res_matrix = [[''] * s_len for _ in range(numRows)]

        # 先遍历列，再遍历行
        for i in range(len(res_matrix[0])):
            for line in range(numRows):
                if index >= s_len:
                    break
                
                # 最左列填满
                if i % (numRows - 1) == 0:
                    res_matrix[line][i] = s[index]
                    index += 1
                # 中间列只填一个
                else:
                    res_matrix[numRows - i % (numRows - 1) - 1][i] = s[index]
                    index += 1
                    break
            
        return ''.join(''.join(res_line) for res_line in res_matrix)

a = Solution()
s = "PAYPALISHIRING"
print(a.convert(s, 3))
