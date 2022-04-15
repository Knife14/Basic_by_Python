"""
title: 连续子数组和
writer: 山客
date: 2021.8.23
key：哈希表，前缀和 ？？？
example：
输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
tips：
① 暴力检索超时 93 / 94
    for i in range(n - 1):
        sum = nums[i]
        j = i + 1
        while j < n:
            sum += nums[j]
            if sum % k == 0:
                return True
            j += 1
"""


class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        # 前缀和+哈希表，查看是否有连续的一段元素的，和为k的倍数就行，同余定理，i%m - j%m = (i-j)%m
        n = len(nums)
        if n < 2:
            return False

        # 记录前缀和，除以k的余数
        sub = [nums[0]]
        for i in range(1, n):
            sub.append((sub[-1] + nums[i]) % k)
        print(sub)

        # 记录相同前缀和对k取余，第一次出现的位置
        dic = {}
        for idx, pre in enumerate(sub):
            if pre not in dic:
                dic[pre] = idx
        print(dic)

        # 查找是否存在一段连续子区间
        # nums[i] 到 nums[dic[sub[i]]] 为 k 的倍数子区间
        # 确保 i - dic[sub[i]] >= 2 即可
        for i in range(2, n):
            if i - dic[sub[i]] >= 2:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([23, 2, 6, 4, 7], 13))
