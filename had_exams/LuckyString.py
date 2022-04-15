"""
title：幸运N串
writer：山客
date：2021.8.5
key：
example：
输入：
3
NNTN
NNNNGGNNNN
NGNNNNGNNNNNNNNSNNNN
输出：
4
10
18
tips：
"""


def LuckyString(nStrs: list):
    counts = []

    for nStr in nStrs:
        tmp = []
        # 非 N 个数小于等于2，默认返回原长度
        if len(nStr) - nStr.count('N') <= 2:
            counts.append(len(nStr))
        else:  # 字符串中超过2个字符不是N
            low = high = 0  # 双指针
            for i in range(len(nStr)):
                if nStr[i] == 'N':
                    high += 1
                    if high == len(nStr) - 1:  # 最后一小段
                        tmp.append(abs(high - low))
                else:  # 当前字符不是N，则意味着字符串被分段
                    tmp.append(abs(high - low))
                    low = high = i
            # 切片，计算最大值
            max = 0
            for i in range(len(tmp) - 2):
                if sum(tmp[i: i + 3]) > max:
                    max = sum(tmp[i: i + 3])
            counts.append(max + 2)

    for count in counts:
        print(count)


if __name__ == '__main__':
    t = int(input())  # 字符串总数
    nStrs = []
    for _ in range(t):
        nStrs.append(input())

    LuckyString(nStrs)