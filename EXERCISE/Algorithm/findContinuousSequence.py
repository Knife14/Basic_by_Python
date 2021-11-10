"""
title: 和为s的连续正数序列
writer: 山客
date: 2021.4.18
key：滑动窗口
example:
输入：target = 9
输出：[[2,3,4],[4,5]]

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""

class Solution:
    def findContinuousSequence(self, target: int) -> list:
        res = []
        i, j = 1, 1  # 滑动窗口的左右边界
        tmp = 0  # 滑动窗口的和

        while i <= target // 2:
            # i最长只能到目标值的一半，由于tar// 2 * 2 + 1 <= target
            if tmp < target:
                tmp += j
                j += 1
            elif tmp > target:
                tmp -= i
                i += 1
            else:
                # tmp == target
                arr = list(range(i, j))
                res.append(arr)
                # 继续移动
                tmp -= i
                i += 1

        return res