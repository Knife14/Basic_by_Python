"""
title：冒泡排序
writer：山客
date：2021.3.26
thinking：相邻的两个元素进行比较，较大的放后面（升序）
          每轮只能保证该轮最末端元素是比较元素中最大的
time：O（n²）
"""


def bubble_Sort(nums: list) ->list:

    l = len(nums)

    for i in range(l - 1):
        for j in range(l - 1 - i):
            # 每轮都从最左端开始进行冒泡排序，排序元素个数逐轮递减
            # 每轮只保证该轮最末端元素是比较元素中最大的
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


if __name__ == '__main__':
    n = [32, 12, 15, 11, 5, 99, 86]
    print(bubble_Sort(n))
