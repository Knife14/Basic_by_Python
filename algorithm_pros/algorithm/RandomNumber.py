"""
title：随机数
writer：山客
date：2021.9.17
problem：
输入：
3
2
2
1
11
10
20
40
32
67
40
20
89
300
400
15
输出：
1
2
10
15
20
32
40
67
89
300
400
...
tips：
① 没看懂这条题的意思……
"""

import random


class Solution:
    def RandomNumber(self, numbers: list) -> list:
        res = [[] for _ in range(len(numbers))]

        for i in range(len(numbers)):
            for _ in range(numbers[i]):
                tmp = random.randint(1, 1001)
                if tmp not in res:
                    res[i].append(tmp)

        return res


if __name__ == '__main__':
    s = Solution()

    numbers = []
    while True:
        try:
            numbers.append(int(input()))
        except:
            break

    ress = s.RandomNumber(numbers)
    for res in ress:
        res.sort()
        for r in res:
            print(r)
