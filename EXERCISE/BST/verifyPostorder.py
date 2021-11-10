"""
title：二叉搜索树的后序遍历序列
writer：山客
date：2021.4.13
key：递归、分治（划分左右子树）
example：
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：

输入: [1,6,3,2,5]
输出: false

示例 2：

输入: [1,3,2,6,5]
输出: true
"""


class Solution:
    def verifyPostorder(self, postorder: list) -> bool:

        def recur(i, j):
            # i为左子树最左节点，j为根节点
            if i >= j:
                # 当i一直递归到与根节点重叠时，都是正常的，那就返回true
                return True
            # 找出左子树的区间 i ~ m - 1
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            # 找到右子树的开始位置
            m = p
            # 找出右子树的区间 m ~ j - 1
            while postorder[p] > postorder[j]:
                p += 1

            # p == j - 判断此树正确
            # recur(i, m - 1) - 判断左子树正确
            # recur(m, j - 1) - 判断右子树正确
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        if recur(0, len(postorder) - 1):
            return True

        return False
