"""
title：两个序列
writer：山客
date：2021.8.16
key：最长连续上升子序列
example：
输入：
4
4 2 3 1
1 2 3 4
输出：
2
tips：
① 不需要考虑具体插入（题目说明可以插入任意位置）
② 移动次数 = 序列长度 - 最大连续上升子序列长度
"""


def TwoList(n: int, init: list, target: list):

    cnt = {}  # 记录目标序列的位置
    for i in range(n):
        cnt[target[i]] = i
    # 将 init 序列中的元素转换为其目标地址
    for i in range(n):
        init[i] = cnt[init[i]]
    print(cnt)
    print(init)

    cnt, ans = 1, 1
    for i in range(1, n):
        # 求最大连续上升子序列长度（地址连续上升）
        if init[i] > init[i - 1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1

    # 移动次数 = 序列长度 - 最大连续上升子序列长度
    return int(n - ans)


if __name__ == '__main__':
    n = int(input())  # 序列长度
    init = input().split()  # 初始序列
    target = input().split()  # 目标序列

    res = TwoList(n, init, target)
    print(res)
