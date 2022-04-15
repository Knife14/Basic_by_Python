"""
title: 打家劫舍②
writer: 山客
date: 2021.4.15
key：动态规划
problem：房子围成了一个圈。
example：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
tips：
① 抢了第一间，就不能抢最后一间
"""


class Solution:
    def rob(self, nums: list) -> int:

        def robRange(start: int, end: int) -> int:
            pre = nums[start - 1]
            cur = max(pre, nums[start])

            # ！！！ 剩余的房间可能少于或等于2，会进不去循环
            for i in range(start + 1, end):
                # 不能抢前一个的，所以比较的是pre + nums[i], cur
                # cur： 左 - n + 1号；右 -   n  号
                # pre： 左 -   n  号；右 - n - 1号
                pre, cur = cur, max(pre + nums[i], cur)

            return cur

        if not nums:
            return 0

        l = len(nums)

        if l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
        else:
            # 每个房子的金额都是非负整数，所以一定会抢0/1号房间
            # 房子围成了一个圈，所以头尾也不能相邻
            # 因此对抢了 0/1 号房间进行分类
            # 0/1号房间的金额可能一样，所以不能简单的加if-else
            return max(robRange(1, l - 1), robRange(2, l))


if __name__ == '__main__':
    s = Solution()
    print(s.rob([2, 1, 1, 1]))
