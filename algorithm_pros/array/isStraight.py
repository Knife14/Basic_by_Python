"""
title: 扑克中的顺子
writer: 山客
date: 2021.4.19
example:
输入: [1,2,3,4,5]
输出: True
"""

# 根据王出现的次数，判断相邻元素能否构成顺子
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        times = 0  # sign the nums of kings

        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] == 0:
                times += 1
            # abs(nums[i] - nums[i - 1]) need to be 
            # between from 0 to (1 + times of kings)
            # besides of it, the abs item need to be bigger than 0
            elif 0 < abs(nums[i - 1] - nums[i]) <= 1 + times:
                # update the times of kings
                times = (1 + times) - abs(nums[i - 1] - nums[i])
            else:
                return False
        
        return True


# 判断最大最小值，差值小于 5 即可
class Solution:
    def isStraight(self, nums: list) -> bool:
        if not nums:
            return False

        repeat = set()
        # 当前最大、最小牌
        large, low = -1, 14

        for num in nums:
            if num == 0:
                # 大小王可以充当任意牌
                continue

            # 更新最大最小牌
            large = max(large, num)
            low = min(low, num)

            # 如果有重复的牌，提前判断不是顺子
            if num in repeat:
                return False
            
            repeat.add(num)

        # 最大最小牌差值小于5即为顺子
        return large - low < 5
