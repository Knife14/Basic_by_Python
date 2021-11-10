"""
title: 删除有序数组中的重复项2
writer: 山客
date: 2021.4.6
key：双指针
example:
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0

        slow = 0

        # 引入双指针，slow、fast

        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        # 返回指针，需要 + 1
        return slow

