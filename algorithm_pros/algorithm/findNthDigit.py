"""
title：数字序列中某一位的数字
writer：山客
date：2021.4.15
problem：
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
example：
输入：n = 3
输出：3

输入：n = 11
输出：0
tips：
① 每数位都有  10**count * 9 * (count+1)  个数
"""


class Solution:
    def findNthDigit(self, n: int) -> int:

        # n 是数位，不是数值

        if n < 10:
            return n

        n -= 9
        # 数位count，如11即两(count + 1)位
        count = 1

        while True:
            # 当前数位的最大位数
            # 当前数位所有情况 = 10 ** count * 9（不算前面数位）
            # 即只有两数位的时候，只算10-99共90个
            # 1-9共10情况不算在内
            # 当前数位的最大数 = 当前数位所有情况 * 当前数位数(count + 1)
            num = (10 ** count) * 9 * (count + 1)

            if n > num:
                # n超出当前最大位数
                n -= num
                count += 1
            else:
                # n未超出当前最大位数，即n在最大位数中
                # divmod() return: i - 商，j  - 余
                # return res
                i, j = divmod(n, count + 1)
                if j:
                    # 有余数
                    # 基数（10 ** count） + 商
                    return int(str(10 ** count + i)[j - 1])
                else:
                    # 没余数
                    # 基数（10**count） + 商 - 1
                    return int(str(10 * count + i - 1)[-1])


