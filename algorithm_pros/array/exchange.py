"""
title：调整数组顺序使奇数位于偶数前面
writer：山客
key：双指针
date：2021.4.8
example：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""


class Solution:
    def exchange(self, nums: list) -> list:
        """
        nums_odd = []
        nums_even = []

        for i in nums:
            if i % 2 == 0:
                nums_even.append(i)
            else:
                nums_odd.append(i)

        return nums_odd + nums_even
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            # 左边为奇数, left += 1
            while left < right and nums[left] % 2 == 1:
                left += 1
            # 右边为偶数, right -= 1
            while left < right and nums[right] % 2 == 0:
                right -= 1
            # 上面两个循环让当时的left、right分别指向偶数、奇数
            # 故调换两者的位置
            nums[left], nums[right] = nums[right], nums[left]
        return nums

