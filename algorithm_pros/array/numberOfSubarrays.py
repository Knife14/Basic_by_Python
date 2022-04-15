"""
title: 统计【优美子数组】
writer: 山客
date: 2021.3.20
example:
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
"""


class Solution:
    """
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
    """
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        find_odd = []  # 奇数(odd)位序
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                find_odd.append(i)
        if len(find_odd) < k:
            # 给定list奇数长度不足k时，判断异常
            return 0
        ol = len(find_odd)
        for i in range(ol):
            j = i + k - 1  # 最小组合的右边界，即组合中只有奇数
            # 由于实际数组中奇数偶数并存，所以还需要考虑偶数个数
            even_left = 0  # 左边连续偶数数量
            even_right = 0  # 右边连续偶数数量
            if j >= ol:
                # 给定list奇数长度不足k时，判断异常，终止执行
                break
            if i - 1 in range(ol):
                # 确保i-1存在
                if find_odd[i] - find_odd[i-1] > 1:
                    # 位序相减，得到的是其中还有几位连续偶数
                    even_left = find_odd[i] - find_odd[i-1] - 1
            else:
                even_left = find_odd[i]
            if j + 1 in range(ol):
                if find_odd[j+1] - find_odd[j] > 1:
                    even_right = find_odd[j+1] - find_odd[j] - 1
            else:
                even_right = len(nums) - find_odd[j] - 1
            # 对于第i个奇数来说，存在子数组[left,right]包含奇数k个，故有left*right
            # 累计i个count[i]
            count += (even_left + 1) * (even_right + 1)
        return count


"""
a = Solution([1,1,2,1,1], 3)
print(a.numberOfSubarrays())
"""
