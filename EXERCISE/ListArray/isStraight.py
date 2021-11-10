"""
title: 扑克中的顺子
writer: 山客
date: 2021.4.19
example:
输入: [1,2,3,4,5]
输出: True
"""


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