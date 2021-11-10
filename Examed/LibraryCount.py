"""
title：图书馆人数
writer：山客
date：2021.8.20
key：
example：
输入：
5 2
1 1 1
2 1 1
3 1 1
4 1 1
5 1 5
输出：
1 0 0 0 0
2 0 0 0 0
2 0 0 0 0
2 0 0 0 0
2 0 0 0 1
tips：
"""


def Library(n: int, K: int, data: list):
    cnt = [[0] * 5 for _ in range(n)]  # 计数
    visited = set()
    studying = set()

    for i in range(n):
        # 正常进楼
        # 边界条件：刷卡进楼、没进过楼、楼层位置有剩余
        if data[i][1] == 1 \
                and str(data[i][0]) not in visited \
                and cnt[i - 1][data[i][2] - 1] < K:
            cnt[i] = cnt[i - 1].copy()
            cnt[i][data[i][2] - 1] += 1
            visited.add(str(data[i][0]))
            studying.add(str(data[i][0]))
        # 正常出楼
        # 边界条件：刷卡出楼、确实在楼中、楼层里确实有人
        elif data[i][1] == 0 \
                and str(data[i][0]) in studying \
                and cnt[i - 1][data[i][2] - 1] > 0:
            cnt[i] = cnt[i - 1].copy()
            cnt[i][data[i][2] - 1] -= 1
            studying.remove(str(data[i][0]))
        # 非正常进楼
        # 边界条件：二次进楼，楼层人数已到达上限
        elif data[i][1] == 1 and (
                str(data[i][0]) in visited
                or cnt[i - 1][data[i][2] - 1] >= K
        ):
            cnt[i] = cnt[i - 1].copy()
            continue
        # 非正常出楼
        # 边界条件：楼层里没有这人
        elif data[i][1] == 0 and str(data[i][0]) in studying:
            cnt[i] = cnt[i - 1].copy()
            continue

    return cnt


if __name__ == '__main__':
    n, K = input().split()
    n, K = int(n), int(K)  # 刷卡记录条数，图书馆每层能容纳人数

    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    res = Library(n, K, data)
    for i in range(n):
        for j in range(5):
            print(res[i][j], end=' ')
        print()
