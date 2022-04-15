"""
title：蚂蚁森林之王
writer：山客
date：2021.8.12
key：从后向前遍历
example：
输入：
4
0 1 1 1
输出：
4
1
1
1
tips：
① 注意对应下标
"""


def ForestKing(n: int, obj: list):
    tickets = [1] * n  # 保底每个小动物有 1 张自己的票

    # 由于只会投给比自己能力值大的，所以循环是 [n - 1: 1]
    for i in range(n - 1, 0, -1):
        if obj[i] > 0:
            # 把 i 身上的票，都给予崇拜对象 obj[i] - 1（从 1 开始算，所以要减 1）
            tickets[obj[i] - 1] += tickets[i]
        print(tickets)

    return tickets


if __name__ == '__main__':
    n = int(input())  # 小动物的数量
    # 第 i 只小动物的崇拜对象 obj[i]
    # 即 obj[i] = m 时，i 崇拜 m
    obj = list(map(int, input().split()))

    res = ForestKing(n, obj)

    for i in res:
        print(i)
