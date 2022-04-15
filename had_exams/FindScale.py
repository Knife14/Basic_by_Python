"""
title：比例问题
writer：山客
date：2021.8.11
key：
example：
输入：
1 1 2 1
1000 500 4 2
输出：
0 0
1000 500
tips：
"""


# 求最大公约数
def Simplify(a: int, b: int):
    m, n = a, b
    while n > 0:
        m, n = n, m % n
    return a // m, b // m


def FindScale(data: list):
    A, B = data[0], data[1]
    mina, minb = Simplify(data[2], data[3])  # 确定比例是最简比

    # resA * b = resB * a ，其中 resA <= A, resB <= B， a 和 b 均为最大公约比形式
    # 故 1 <= resA * b = resB * a <= min(A * b, B * a)
    # 则可得最简比的最大倍数 = min(A * b, B * a) // (a * b)
    C = min(A * minb, B * mina) // (mina * minb)

    return C * mina, C * minb


if __name__ == '__main__':
    data = list(map(int, input().split()))

    resa, resb = FindScale(data)

    print(str(resa) + ' ' + str(resb))
