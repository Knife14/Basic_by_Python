"""
title：搜索旋转排序数组①
writer：山客
date：2021.4.7
key：二分查找
example：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
tips：
①针对原有序排列数组，可以用二分法查找，时间复杂度是O(n)= nlogn
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # 0 -> mid 升序，不一定遇到最大值            
            if nums[0] <= nums[mid]:
                # 只有在target大于nums[0]以及小于mid索引值时
                # target一定在mid左边
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                # target 大于mid索引值时，一定会在mid右边
                # target 小于mid索引值时，却不一定会在mid的左边，即if的条件
                else:
                    left = mid + 1
            # 0 -> mid 先升序后遇到最大值
            else:
                # 只有 target 大于mid索引值并且小于nums[-1]值时
                # target一定会在mid右边
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                # target小于mid索引值时，target一定在mid左边
                # target大于mid索引值时，target不一定在mid的左边，即if的条件
                else:
                    right = mid - 1
        
        return -1

a = Solution()
n = [4,5,6,7,0,1,2]
print(a.search(n, 3))
