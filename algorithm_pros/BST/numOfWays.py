"""
title: 将子数组重新排序得到同一个二叉查找树的方案数
writer: 山客
date: 2021.3.22
problem:
给你一个数组 nums 表示 1 到 n 的一个排列。
我们按照元素在 nums 中的顺序依次插入一个初始为空的二叉查找树（BST）。
请你统计将 nums 重新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 nums 原本数字顺序得到的二叉查找树相同。
example:
输入：nums = [2,1,3]
输出：1
解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。

输入：nums = [3,4,5,1,2]
输出：5
解释：下面 5 个数组会得到相同的 BST：
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

thinking:
动态规划：根据乘法原理，可以得到状态转移方程为：f[ai] = C * f[ail] * f[air]
          若ai子树为空，则size为0，f即为1。
组合计数：排列组合 C
"""


class TNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.size = 1
        self.ans = 0


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def insert(val: int):
            cur = root  # 根节点
            while 1:
                cur.size += 1
                if val >= cur.value:
                    if not cur.right:
                        # 该节点的右子树不存在，则新增
                        cur.right = TNode(val)
                        return
                    # 结点跳到下一层
                    cur = cur.right
                elif val < cur.value:
                    if not cur.left:
                        cur.left = TNode(val)
                        return
                    # 结点跳到下一层
                    cur = cur.left

        def dfs(node: TNode):
            if not node:
                # 若结点不存在
                return
            dfs(node.left)
            dfs(node.right)
            # 嵌套if，若左、右子树存在。size - 长度 ，ans - 排列可能数
            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1
            node.ans = c[lsize+rsize][lsize] * lans * rans % mod


        mod = 1_000_000_007
        n = len(nums)
        if n == 0:
            return 0
        c = [[0] * n for _ in range(n)]
        c[0][0] = 1
        for i in range(1, n):
            c[i][0] = 1
            for j in range(1, n):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod
        root = TNode(nums[0])
        # 建立最初的二叉树
        for i in range(1, n):
            val = nums[i]
            insert(val)

        dfs(root)

        return (root.ans - 1 + mod) % mod