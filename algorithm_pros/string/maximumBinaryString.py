"""
title: 修改后的最大二进制字符串
writer: m14
date: 2024.4.10
key：'00' -> '10' 该变换为赚， '10' -> '01' 该变换为亏
example:
输入：binary = "000110"
输出："111011"
解释：一个可行的转换为：
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"
thinking：
1. 先找到第一个非1的0位置
2. 输出结果至多有一个0
"""

class Solution:
    def maximumBinaryString_directbuild(self, binary: str) -> str:
        l = len(binary)

        i = 0
        result = ""
        while i < l and binary[i] == '1':
            result += binary[i]
            i += 1
        
        cnt_0 = binary[i:].count('0')
        if cnt_0 < 2:
            return binary
        
        return result + '1' * (cnt_0 - 1) + '0' + '1' * (l - i - cnt_0)

    def maximumBinaryString_greedy(self, binary: str) -> str:
        binary = list(binary)
        l = len(binary)

        i = j = 0
        while i < l:
            if binary[i] == '1':
                i += 1
                continue
            
            while j <= i or (j < l and binary[j] == '1'):
                j += 1
            # confirm index_j in the range of binary
            # more than 1 piece of '0' in this binary[i:]
            if j < l:
                binary[i] = '1'
                binary[j] = '1'
                binary[i + 1] = '0'
            
            i += 1

        return ''.join(binary)
