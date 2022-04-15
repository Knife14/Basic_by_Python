"""
title：二进制数计数
writer：山客
date：2021.8.5
key：
split() / map() / bin() / count()
example：
输入：
1
5
8 3 5 7 2
输出：
3
tips：
① 类型转换 str -> int -> str
"""


def BinaryCount(data: list, n: int):
    if n == 0:
        return 0

    data = list(map(str, [bin(num) for num in data]))  # 转为二进制显示，bin对int型有效
    counts = {}
    # print(data)
    for num in data:
        count = num.count('1')  # 计算字符串中有多少个1，count对str型有效
        if count not in counts:
            counts[count] = 1
        else:
            counts[count] += 1

    return len(counts)


if __name__ == '__main__':
    t = int(input())  # 样例数

    for i in range(t):
        n = int(input())  # 单个样例所含数个数
        data = list(map(int, input().split()))  # 输入单个样例中具体数值
        res = BinaryCount(data, n)
        print(res)
