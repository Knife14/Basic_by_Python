"""
title: 二叉搜索树的第k大节点
writer: 山客
date: 2021.4.18
example:
输入:
root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS + 中序遍历（右中左），根据k值的递减归零提前退出
# 时间复杂度： O（N）  空间复杂度：O（N）
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = -1

        def dfs(curr: TreeNode):
            if not curr:
                return 

            dfs(curr.right)

            # quit dfs(curr.left) or more dfs(curr.right) when self.k == 0
            if self.k == 0:
                return
            self.k -= 1
            # after self.k - 1 == 0, it get the res
            if self.k == 0:
                self.res = curr.val

            dfs(curr.left)

        dfs(root)
        return self.res
      
      
# 遍历整颗树然后进行排序
# 空间复杂度：O（N）   时间复杂度：O（2N）
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:

        if not root:
            return 0

        vals = []

        def dfs(root: TreeNode):

            if not root:
                return

            vals.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        vals = sorted(vals)

        return vals[len(vals) - k + 1]
