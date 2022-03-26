"""
title：把字符串转换成整数
writer：山客
date：2021.7.29
example：
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
"""

# 一个比较简单好理解的转换写法    ————     注意越界！
# 时间复杂度：O（N）   空间复杂度：O（N）
class Solution:
    def strToInt(self, str: str) -> int:
        ss = str.lstrip()

        # special situation
        if len(ss) == 1:
            if ss == '+' or ss == '-':
                return 0
            else:
                return int(ss)
        elif len(ss) == 0:
            return 0

        res = []
        for i in range(len(ss)):
            # handler + or -
            if i == 0:
                if ss[0] == '+' or ss[0] == '-':
                    res.append(ss[0])
                    continue
                elif not ss[i].isdigit():
                    return 0

            if ss[i].isdigit():
                res.append(ss[i])
            else:  # just need int
                break
        
        try:
            res = int(''.join(res))
        except:
            return 0

        # hanlder the max or the min
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < - 2 ** 31:
            return - 2 ** 31
        else:
            return res

# 一个整理的比较好的判断方法，设置正负标志位
# 时间复杂度：O（N）   空间复杂度：O（N）
class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()                      # 删除首尾空格

        if not str:
            return 0                   # 字符串为空则直接返回

        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10

        if str[0] == '-':
            sign = -1            # 保存负号
        elif str[0] != '+':
            i = 0              # 若无符号位，则需从 i = 0 开始数字拼接

        for c in str[i:]:
            if not '0' <= c <= '9':
                break     # 遇到非数字的字符则跳出
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min  # 数字越界处理
            res = 10 * res + ord(c) - ord('0')  # 数字拼接

        return sign * res


if __name__ == '__main__':
    s = Solution()
    print(s.strToInt("   -42"))
