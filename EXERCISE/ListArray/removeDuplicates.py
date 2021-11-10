"""
title: 删除有序数组中的重复项
writer: 山客
date: 2021.4.6
example:
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if not nums:
            return 0

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))