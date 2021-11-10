"""
title：春游
writer：山客
date：2021.8.11
key：
example：
输入：
2
4
2 10 12 11
4
2 3 7 8
输出：
37
19
tips：
"""


def SpringOut(data: list):
    data = sorted(data)  # 升序
    l = len(data)

    res = 0

    while l >= 4:
        # 当剩余人数大于等于4人时，有两种过河方法：
        # ① 最轻的带最重的过去，然后最轻的回来
        # ② 最轻的和次轻的先过去，然后最轻的回来，两个最重的再过去，次轻的回来
        res += min(
            2 * data[0] + data[l - 1] + data[l - 2],
            data[0] + 2 * data[1] + data[l - 1]
        )
        l -= 2

    # 当剩余人数小于4时
    if l == 3:
        res += data[0] + data[1] + data[2]
    elif l == 2:
        res += data[1]
    elif l == 1:
        res += data[0]

    return res


if __name__ == '__main__':
    T = int(input())  # 一共有 T 组测试数据
    data = [[] for _ in range(T)]

    for i in range(T):
        n = int(input())  # 该组人数
        data[i] += list(map(int, input().split()))

    for tmp in data:
        print(SpringOut(tmp))
