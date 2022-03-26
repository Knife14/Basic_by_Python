"""
title：构建乘积数组
writer：山客
date：2021.7.29
example：
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
"""

# 双指针：
# i负责正序遍历，记录每个点（0 -> len(a) - 1）的左边乘积
# j负责反序遍历，记录每个点（len(a) - 1 -> 0）的右边乘积
# 时间复杂度： O（N）   空间复杂度：O（N）
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if not a:
            return []

        left, right = 1, 1
        i, j = 0, len(a) - 1
        res = [1] * len(a)

        while i < len(a):
            res[i] *= left  # Get the product of the left of i

            # update left
            left *= a[i]
            i += 1

            res[j] *= right  # Get the right of i

            # update right
            right *= a[j]
            j -= 1
        
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.constructArr([1,2,3,4,5]))
