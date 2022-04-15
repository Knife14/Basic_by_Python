"""
title：归并排序
writer：山客
date：2021.3.26
time：O（nlog(n)
thinking：先递归分解数组，
          再合并数组
tips：
①分治法
"""


def merge_sort(nums: list):

    if len(nums) == 1:
        # 长度等于1，无法分解，直接返回
        return nums

    l = len(nums) // 2

    # 将数组分解到最小规模-分治法
    left = merge_sort(nums[:l])
    right = merge_sort(nums[l:])

    return sort(left, right)


def sort(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 确保所有元素进入新的有序队列
    # 一般是left/right的最后一个未加入判断的元素
    result += left[i:]
    result += right[j:]
    """
    python数组的合并
    *****
    input:
    a = [1,2]
    b = [1,2,4,5]

    print(a + b[2:])

    a.append(b[2:])
    print(a)
    
    output:
    -> [1, 2, 4, 5]
    -> [1, 2, [4, 5]]
    *****
    """

    return result


if __name__ == '__main__':
    n = [32, 12, 15, 11, 5, 99, 86]
    print(merge_sort(n))
