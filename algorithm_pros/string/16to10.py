"""
title：进制转换
writer：山客
date：2021.9.17
problem：
输入：
0xA
0xAA
输出：
10
170
"""


class Solution:
    def _16to10(self, numbers: list) -> list:
        res = []

        for number in numbers:
            tmp = 0
            cnt = 0
            for i in range(len(number) - 1, -1, -1):
                if number[i] == 'x':
                    break

                if number[i] == 'A':
                    curr = 10
                elif number[i] == 'B':
                    curr = 11
                elif number[i] == 'C':
                    curr = 12
                elif number[i] == 'D':
                    curr = 13
                elif number[i] == 'E':
                    curr = 14
                elif number[i] == 'F':
                    curr = 15
                else:
                    curr = int(number[i])

                tmp += (16 ** cnt) * curr

                cnt += 1

            res.append(tmp)

        return res


if __name__ == '__main__':
    s = Solution()

    numbers = []
    while True:
        try:
            numbers.append(input())
        except:
            break

    ress = s._16to10(numbers)
    for res in ress:
        print(res)
