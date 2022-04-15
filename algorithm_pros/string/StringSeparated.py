"""
title：字符串分隔
writer：山客
date：2021.9.17
problem：
输入：
abc
123456789
输出：
abc00000
12345678
90000000
"""


class Solution:
    def StringSeparated(self, messages: list) -> list:
        res = []

        for message in messages:
            while message:
                if len(message) >= 8:
                    res.append(message[:7])
                    message = message[8:]
                else:
                    cnt = 8 - len(message)
                    message += '0' * cnt
                    res.append(message)
                    break

        return res


if __name__ == '__main__':
    messages = []

    while True:
        try:
            messages.append(input())
        except:
            break

    s = Solution()
    ress = s.StringSeparated(messages)
    for res in ress:
        print(res)
