"""
title：最小数
writer：山客
date：2021.4.18
example：
输入：nums = [10,2]
输出："102"

输入：nums = [3,30,34,5,9]
输出："3033459"
"""


class Solution:
    def minNumber(self, nums: list) -> str:

        res = ""
        # map() 对数组元素作映射，即nums[i] -> fun(nums[i])
        nums = list(map(str, nums))

        # 比较，使得nums_str按最大数要求降序排序
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        for i in range(len(nums)):
            res += nums[i]

        if res == '0':
            return '0'

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minNumber([3, 30, 34, 5, 9]))