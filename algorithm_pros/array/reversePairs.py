"""
title: 数组中的逆序对
writer: 山客
date: 2021.7.29
example：
输入: [7,5,6,4]
输出: 5
"""


class Solution:
    def reversePairs(self, nums: list) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r:
                return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1  # 统计逆序对
            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([7,5,6,4]))