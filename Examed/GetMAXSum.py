"""
title：找到字符串中出现次数最多的数字
writer：山客
date：2021.8.9
key：
example：
输入：
9fil3dj11P0jAsf11j
输出：
22
tips：
"""


def GetMAXSum(s: str):
    count = {}  # 数字出现计数
    low = high = 0  # 双指针

    for i in range(len(s)):
        if s[i] <= '9' and s[i] >= '0':
            high += 1
        else:
            if low != high:
                if s[low: high] not in count:
                    count[s[low: high]] = 1
                else:
                    count[s[low: high]] += 1
            low = i + 1
            high = i + 1

    count = sorted(count.items(), key=lambda x: x[1])
    tmp = count.pop()

    return int(tmp[0]) * tmp[1]


if __name__ == '__main__':
    s = input()
    print(GetMAXSum(s))
