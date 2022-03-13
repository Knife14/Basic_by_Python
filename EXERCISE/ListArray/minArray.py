"""
title: 旋转数组的最小数字
writer: 山客
date: 2021.4.2
example:
输入：[3,4,5,1,2]
输出：1

输入：[2,2,2,0,1]
输出：0
"""

# 二分法：由于本身是一个升序数组，
# 若m位元素比j位元素要大，可以根据原来升序的定义，确定m的左边都比j位元素大
# 即最小元素，一定是在m位的右边
# 时间复杂度： O（logN）    空间复杂度：O（1）
class Solution:
    def minArray(self, numbers: list) -> int:
        i, j = 0, len(numbers) - 1
        
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            elif numbers[mid] < numbers[j]:
                j = mid
            else:
                j -= 1
        
        return numbers[i]
