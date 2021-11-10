"""
title：二叉树
writer：山客
date：2021.8.14
key：卡特兰数列
example：
输入：
3 3
输出：
5（树的可能数）
tips：
① 状态转移方程（动态规划）应限制树的高度
"""

mod = 1_000_000_007


def BinaryTree(n: int, m: int):  # 节点数 n , 树最大高度 m
    # 初始化
    # 结点个数 n 为 0 时，所有可能的高度m都只能为 1
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 1

    # # dp[i][j] = dp[i-(i-1)-1][j-1] * dp[(i-1)]dp[j-1] + ...
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for left in range(i):
                # j - 1 层的节点数为 i
                # 左子树节点边界为 left ，右子树节点即 i - (left + 1)
                dp[i][j] += dp[left][j - 1] * dp[i - left - 1][j - 1]

    return dp[-1][-1] % mod


if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)

    res = BinaryTree(n, m)
    print(int(res))
