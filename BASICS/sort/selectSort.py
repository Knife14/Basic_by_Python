"""
title：选择排序
writer：山客
date：2021.3.26
time：O（n²）
thinking：第i轮第i位以后的元素分别与i元素作比较，
          较小的与i元素交换位置。（升序）
"""


def select_sort(nums):

    l = len(nums)

    for i in range(l - 1):
        for j in range(i + 1, l):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


if __name__ == '__main__':
    n = [32, 12, 15, 11, 5, 99, 86]
    print(select_sort(n))
