"""
title：堆排序（降序）
writer：山客
date：2021.4.6
thinking：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
          将其与末尾元素进行交换，此时末尾就为最大值。
tips：
①一般来说，大顶堆作升序，小顶堆作降序
time：O(nlogn)
"""


def sift_down(nums: list, begin, end):
    # 向下筛选，j为i的左子节点
    i, j = begin, begin * 2 + 1
    temp = nums[begin]

    while j < end:
        if j + 1 < end and nums[j] < nums[j + 1]:
            # 如果左子节点大于右子节点，则将j指向右子节点
            j += 1
        if temp < nums[j]:
            # 插入值n小于左右子节点
            # 此时j位置的数值最小，即让j上移成为父节点
            # 循环结束后，num[i]的值应该是最小的，tmp的值是最大的
            nums[i] = nums[j]
            i, j = j, j * 2 + 1
        else:
            break

    # 将tmp和根节点交换，交换后nums[i]是最大的
    nums[i] = temp


def heap_sort(nums: list) -> list:

    new_nums = []

    for i in range(len(nums)//2 - 1, -1, -1):
        # 构造堆序 - 大顶堆
        sift_down(nums, i, len(nums))

    for i in range(len(nums) - 1, -1, -1):
        # 进行堆排序，i ：len(nums) - 1 -> 0，逐层递减

        # 由于是大顶堆，所以向下筛选的首项元素就是最大的，直接append即可
        new_nums.append(nums[0])
        # 始终交换栈顶元素与末尾元素，每一步都能确定末尾元素
        # 所以循环次数递减
        # 最后一次循环将会break，确保剩下的元素加入到new_nums中
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, 0, i)

    return new_nums


if __name__ == '__main__':
    n = [32, 12, 15, 11, 5, 99, 86]
    print(heap_sort(n))