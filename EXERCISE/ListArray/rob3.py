"""
title: 打家劫舍③
writer: 山客
date: 2021.4.15
key：动态规划，递归
example：
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
tips：
① 递归函数返回的是一个数组，递归深度越浅，放的位置越前
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:

        def robRange(root: TreeNode):
            if not root:
                return 0, 0

            left = robRange(root.left)
            right = robRange(root.right)

            # 只能偷一层，邻接上下层不能同时偷
            # 偷根节点层
            val1 = root.val + left[1] + right[1]
            # 偷子树层
            val2 = max(left) + max(right)
            return val1, val2

        return max(robRange(root))
