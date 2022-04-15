"""
title：存在重复元素③
writer：山客
date：2021.4.17
key：滑动窗口
example：
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
tips：
① sortedSet() 内部有序的数据结构
② 数组中是否存在一个大小不超过 k 的子数组，该子数组内的最大值和最小值的差不超过 t。
"""

from sortedcontainers import SortedSet
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        if not nums:
            return False

        st = SortedSet()
        left, right = 0, 0

        while right < len(nums):

            if right - left > k:
                st.remove(nums[left])
                left += 1

            # 二分查找有序序列，并且返回插入该元素
            # 在 首个st[n] >= nums[right] - t 的条件下
            # 插入位置为index = n - 1，value = st[index]
            # st[index] < nums[right] - t
            index = bisect.bisect_left(st, nums[right] - t)

            if st and index >= 0 and index < len(st) and abs(st[index] - nums[right]) <= t:
                return True

            st.add(nums[right])
            # 保证检索数组长度不超过k
            right += 1

        return False
