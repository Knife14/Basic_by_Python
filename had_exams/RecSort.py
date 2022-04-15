"""
title：矩形排序
writer：山客
date：2021.8.6
key：
example：
输入：
2
2 2 1 1
输出：
1 1 2 2
tips：
① 5 / 10
"""


def RecSort(n: int, data: list):
    dict_data = {}  # 切片字典
    index = 0  # i - 下标
    for m in range(n):
        dict_data[m] = data[index: index + 2]
        index += 2

    # 排序
    tmp = sorted(dict_data.values(), key=lambda x: x[0] * x[1], reverse=False)
    for i in range(len(tmp) - 1):
        if tmp[i][0] * tmp[i][1] == tmp[i + 1][0] * tmp[i + 1][1]:
            # 宽高比
            if min(tmp[i][0] / tmp[i][1], tmp[i][1] / tmp[i][0]) < \
                    min(tmp[i + 1][0] / tmp[i + 1][1], tmp[i + 1][1] / tmp[i + 1][0]):
                tmp[i][0], tmp[i][1], tmp[i + 1][0], tmp[i + 1][1] = \
                    tmp[i + 1][0], tmp[i + 1][1], tmp[i][0], tmp[i][1]
            # 宽度
            elif min(tmp[i][0] / tmp[i][1], tmp[i][1] / tmp[i][0]) == \
                    min(tmp[i + 1][0] / tmp[i + 1][1], tmp[i + 1][1] / tmp[i + 1][0]):
                if tmp[i][0] < tmp[i + 1][0]:
                    tmp[i][0], tmp[i][1], tmp[i + 1][0], tmp[i + 1][1] = \
                        tmp[i + 1][0], tmp[i + 1][1], tmp[i][0], tmp[i][1]

    for j in range(n):
        if j == n - 1:
            print(str(tmp[j][0]) + " " + str(tmp[j][1]))
        else:
            print(str(tmp[j][0]) + " " + str(tmp[j][1]), end=' ')


if __name__ == '__main__':
    n = int(input())  # 矩形个数
    data = list(map(int, input().split()))  # 每个矩形具体长宽

    RecSort(n, data)
