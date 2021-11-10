"""
title: 132模式
writer: 山客
date: 2021.3.24
example:
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。

输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
"""

class Solution:
    def find132pattern(self, nums) -> bool:
        l = len(nums)

        if l < 3:
            return False

        # 从最左边开始遍历，如果存在132组合，即返回true
        left_min = nums[0]
        count = 0

        for i in nums:
            count += 1
            if left_min < i:
                for j in nums[count:]:
                    if i > j and j > left_min:
                        return True

            left_min = min(left_min, i)

        return False

a = Solution()
b = a.find132pattern([3,1,4,2])
print(b)


"""
import sortedcontainers

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = SortedList(nums[2:])
        
        for j in range(1, n - 1):
            if left_min < nums[j]:
                # bisect_right()  对有序的数字升序序列进行快速排序查找
                index = right_all.bisect_right(left_min)  # right_all[index] > left_min 
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False

"""