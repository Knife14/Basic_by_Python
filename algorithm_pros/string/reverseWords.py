"""
title: 翻转单词顺序
writer: 山客
date: 2021.8.27
example:
输入: "the sky is blue"
输出: "blue is sky the"
tips：
① 两种做法：正序遍历、倒序遍历都可
"""


class Solution:
    # 倒叙
    def reverseWords1(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = ""

        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1  # 搜索首个空格

            res += s[i + 1: j + 1]  # 添加单词
            if i > 0:
                res += ' '

            while s[i] == ' ':
                i -= 1  # 跳过单词间空格

            j = i  # j 指向下个单词的尾字符

        return res

    # 正序
    def reverseWords2(self, s: str) -> str:
        s_list = []

        low = high = 0

        while high < len(s):
            if s[high] != ' ':
                high += 1
            # 识别空格
            else:
                if low != high:
                    s_list.append(s[low: high])
                    high = high + 1
                    low = high
                else:
                    high = high + 1
                    low = high

            # 处理最后一段字符串
            if high == len(s) - 1 and s[-1] != ' ':
                s_list.append(s[low:])

        s_list = reversed(s_list)
        return ' '.join(s_list)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords1("the sky is blue"))
