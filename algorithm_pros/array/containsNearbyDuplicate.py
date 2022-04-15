"""
title：存在重复元素②
writer：山客
date：2021.4.17
example：
输入: nums = [1,2,3,1], k = 3
输出: true

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
tips：
① 超时做法：线性搜索、二叉搜索树
② 标准做法：散列表
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        if not nums:
            return False

        map = {}

        for i in range(len(nums)):
            # i 为 位置下标

            # 还未保存已经访问过的节点
            if nums[i] not in map:
                map[nums[i]] = i
            # 已有节点保存过，求差返回要求值
            else:
                if i - map[nums[i]] <= k:
                    return True
                else:
                    # 如果差值不符，记录新的重复值位置下标
                    map[nums[i]] = i

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))