"""
title：水平线
writer：山客
date：2021.8.5
key：
① 双指针？ / 直接遍历？目前只过了 1 / 10
example：
输入：
10
6 12 20 14 15 15 7 19 18 13
6
15 23 19 1 17 24
输出：
2
0
1
1
2
0
tips：
"""


def ansCount(n: int, a: list, q: int, y: list):
    counts = [0] * q
    """
    # 直接遍历
    for i in range(q):
        for j in range(1, n):
            if a[j] <= y[i]:
                continue
            else:
                if a[j - 1] > y[i]:
                    if counts[i] == 0:
                        counts[i] = 1
                    continue
                else:
                    counts[i] += 1
    """
    for i in range(q):
        low = high = 0  # 双指针
        for j in range(n):
            if low == 0 and high == n - 1:  # 若全部基站还把都比洪水要高，则返回 1
                counts[i] = 1
            if a[j] > y[i]:
                high += 1
            else:
                if low != high:  # low != high，意味着该区间的基站是仍然行动的，并且形成一个集群
                    counts[i] += 1
                low = high = j

    for count in counts:
        print(count)


if __name__ == '__main__':
    n = int(input())  # 输入发电站总个数
    a = list(map(int, input().split()))  # 具体发电站海拔高度
    q = int(input())  # 未来洪水数
    y = list(map(int, input().split()))  # 具体洪水海拔高度

    ansCount(n, a, q, y)
