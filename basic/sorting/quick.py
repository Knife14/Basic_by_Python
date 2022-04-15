"""
title：快速排序
writer：山客
date：2021.3.26
key：递归
time：O（nlog(n)）
thinking：通过一趟排序将要排序的数据分割成独立的两部分，
          其中一部分的所有数据都比另外一部分的所有数据都要小，
          然后再按此方法对这两部分数据分别进行快速排序
tips:
①先选一个基准：一般选第一个
"""


def quick_sort(nums, start, end):
    if start >= end:
        # 即意味着分块只剩下1个元素，无需排序，直接返回
        return

    # 位置
    low = start
    high = end

    # 基准 pivot
    piv = nums[low]

    while low != high:
        # 从右往左，当找到在piv右边的值，且大于piv时暂停
        while low < high and piv < nums[high]:
            high -= 1

        if high > low:
            # 确保不越界，再进行交换
            nums[low] = nums[high]
            low += 1

        # 从左往右开始，当找到在piv左边的值，且小于piv时暂停
        while low < high and piv > nums[low]:
            low += 1

        if high > low:
            # 确保不越界，再进行交换
            nums[high] = nums[low]
            high -= 1

    # 确认基准位置，此时low == high，即在中间
    nums[low] = piv

    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)


if __name__ == '__main__':
    n = [32, 12, 15, 11, 99, 5, 86]
    quick_sort(n, 0, len(n) - 1)
    print(n)
