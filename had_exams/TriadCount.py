"""
title：递增三元子序列
writer：山客
date：2021.9.4
key：
example：
输入：
6
2 3 5 4 3 3
输出：
6
tips：
① 暴力检索会超时
"""


def TriadCount(n: int, A: list):
    cnt = 0

    if len(A) < 3:
        return 0

    for i in range(1, n - 1):
        l, r = 0, n - 1
        lc, rc = 0, 0
        piv = A[i]

        while l < i:
            if piv >= A[l]:
                lc += 1
            l += 1

        while r > i:
            if piv <= A[r]:
                rc += 1
            r -= 1

        if lc != 0 and rc != 0:
            cnt += lc * rc

    return cnt


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    res = TriadCount(n, A)
    print(res)
