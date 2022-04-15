"""
title：合法连续子段
writer：山客
date：2021.8.16
key：双指针、数组窗口
example：
输入：
5 2
1 2 1 2 3
输出：
5
tips：
① 在最小区间不变的情况下，求子集数量
"""


def ContinuousPeriod(n: int, m: int, data: list):
    res = 0

    cnt = [0] * 10
    cnt[data[0]] = 1  # 记录出现的次数

    high = 1  # 双指针
    for low in range(1, n + 1):
        if high <= n and cnt[data[high - 1]] < m:
            high += 1
            # 若一直遍历到 high > n 则意味着没有出现符合条件的区间
            while high <= n:
                cnt[data[high - 1]] += 1
                # 当出现次数满足不小于m时，退出循环
                if cnt[data[high - 1]] >= m:
                    break
                high += 1
        # 子集求法：最小区间不变，在最后逐渐 + 1
        # 可换算为 n - high + 1
        res += (n - high + 1)
        cnt[data[low - 1]] -= 1  # ？？？

    return res


if __name__ == '__main__':
    n, m = input().split()  # 数组长度，出现次数
    n, m = int(n), int(m)

    data = list(map(int, input().split()))

    res = ContinuousPeriod(n, m, data)
    print(res)
