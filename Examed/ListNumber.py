"""
title：数组中两个元素和小于等于M的组合数
writer：山客
date：2021.8.21
key：
example：
输入：
7 -1 -1
9
输出：
3
tips：
"""


def ListNum(data: list, M: int):
    res = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] <= M:
                res += 1

    return res


if __name__ == '__main__':
    data = list(map(int, input().split()))
    M = int(input())

    res = ListNum(data, M)
    print(res)


"""
L = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z'
        ]
"""