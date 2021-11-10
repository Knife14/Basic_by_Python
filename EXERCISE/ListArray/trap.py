"""
title: 直方图水量
writer: 山客
date: 2021.4.2
Key：双指针
problem：
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量？
直方图的宽度为 1。
由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。
example:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
thinking：
①引入双指针，来代表当前水槽左右地址和高度
"""


class Solution:
    def trap(self, height: list) -> int:
        res = 0

        N = len(height)

        if N < 2:
            return 0

        left_index, right_index = 0, N - 1  # 左右地址
        left_height, right_height = 0, 0  # 左右高度

        while left_index < right_index:  # 左右指针分别向中间靠拢

            if height[left_index] < height[right_index]:
                # 确保最右的height始终大于最左的height
                if height[left_index] < left_height:
                    # left_height_index < left_now_index，即左高右矮
                    # 根据木桶效应，取差值即可知装多少水
                    res += left_height - height[left_index]
                else:
                    left_height = height[left_index]
                left_index += 1
            else:
                if height[right_index] < right_height:
                    # right_height_index < right_now_index，即右高左矮
                    res += right_height - height[right_index]
                else:
                    right_height = height[right_index]
                right_index -= 1

        return res
