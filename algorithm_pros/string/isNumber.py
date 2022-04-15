"""
title：表示数值的字符串
writer：山客
date：2021.4.7
problem：
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如：
字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)
        index = 0
        has_num = has_e = has_sign = has_dot = False

        while index < n and s[index] == ' ':
            index += 1

        while index < n:

            while index < n and '0' <= s[index] <= '9':
                # 纯数字部分连续遍历
                index += 1
                has_num = True

            if index == n:
                break

            if s[index] == 'e' or s[index] == 'E':
                if has_e or not has_num:
                    # 连续两个e的情况下，或只有e的情况下，返回false
                    return False
                has_e = True
                has_num = has_sign = has_dot = False
            elif s[index] == '+' or s[index] == '-':
                if has_sign or has_num or has_dot:
                    # 若已有dot，再有+-号，则返回false
                    return False
                has_sign = True
            elif s[index] == '.':
                if has_dot or has_e:
                    # e和小数点后面不能再有小数点
                    return False
                has_dot = True
            elif s[index] == ' ':
                break
            else:
                return False

            index += 1

        while index < n and s[index] == ' ':
            index += 1

        return has_num and index == n
