"""
title：希尔排序
writer：山客
date：2021.3.26
time：O（nlog(n)） ~ O（n²）
thinking：将数组列在一个表中并对 列 分别进行插入排序，
          重复这过程，每轮列的步长都会增加，直至最后一列。
"""


def shell_sort(nums: list) -> list:

    l = len(nums)
    # 初始步长
    gap = int(l / 2)

    while gap:
        # 按步长
        for i in range(gap, l):
            j = i
            while j >= gap and nums[j - gap] > nums[j]:
                # 插入排序，从右往左
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap

        # 更新步长
        gap = int(gap / 2)

    return nums


if __name__ == '__main__':
    n = [32, 12, 15, 11, 5, 99, 86]
    print(shell_sort(n))
