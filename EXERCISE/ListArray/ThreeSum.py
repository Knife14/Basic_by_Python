"""
title: 三数之和
writer: 山客
date: 2021.8.23
key：
example:
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]

输入：nums = [0]
输出：[]
"""


class Solution:
    def threeSum(self, nums:list) -> list:
        nums = sorted(nums)
        n = len(nums)
        res = []

        if n < 3:
            return res

        for i in range(n):
            # 若左指针与前一个遍历过的元素相同，需要跳过
            # 防止同样的结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = n - 1  # 从右边开始遍历
            target = -nums[i]
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 防止越界
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([1, -1, -1, 0]))
