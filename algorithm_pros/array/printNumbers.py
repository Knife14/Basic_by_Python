"""
title: 打印从1到最大的n位数
writer: 山客
date: 2021.4.5
example:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
"""

# 直接遍历：遍历个数为 10 ** n - 1
# 时间复杂度： O(2^n)
class Solution:
    def printNumbers(self, n: int) -> list:
        nums = []

        for i in range(1, 10 ** n):
            nums.append(i)

        return nums

# 先统计出会打印多少数值：根据 9 + 10 ** （ n - 1 ）
# 时间复杂度：O(n)
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        nums = 0

        for i in range(1, n + 1):
            if i == 1:
                nums += 9
                continue

            nums += 9 * (10 ** (i - 1))

        return list(range(1, nums + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.printNumbers(2))
