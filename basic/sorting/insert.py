"""
title：插入排序
writer：山客
date：2021.3.26
time：O（n²）
thinking：构建一个有序序列，
          逐个对乱序数据，在有序序列中从后向前排序，
          找到对应的位置并且插入有序序列中。(升序）
"""


def insert_sort(nums):
    l = len(nums)

    for i in range(1, l):
        for j in range(i, 0, -1):
            # 从后向前排序
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]

    return nums

if __name__ == '__main__':
    n = [32, 12, 15, 11, 99, 5, 86]
    print(insert_sort(n))
