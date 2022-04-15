"""
title：纸张分配问题
writer：山客
date：2021.8.21
key：
example：
输入：
4 4 5
输出：
9
tips： 60 %
"""


def PaperProblem(data: list):
    cnt = {}  # 小孩计数
    res = 0

    if len(data) == 1:
        return 1

    for i in range(len(data)):
        if data[i] not in cnt:
            cnt[data[i]] = [i]
        else:
            cnt[data[i]].append(i)

    cnt = dict(sorted(cnt.items()))
    minAge = min(data)
    curr = 1  # 当前只派一张
    for k, v in cnt.items():
        if k == minAge:
            res += len(v)
        else:
            curr += 1
            # 若大于3，则意味着有可能存在中间区间相邻的同年龄的孩子
            # 对于这类孩子，只需要给1张纸即可
            if len(v) >= 3:
                res += curr  # 头 / 尾一定要给一次 curr 张
                tmp = 1
                for i in range(1, len(v) - 1):
                    if v[i] - 1 == v[i - 1] and v[i] + 1 == v[i + 1]:
                        res += 1
                    else:
                        tmp += 1
                        res += tmp
            else:
                res += curr * len(v)

    return res


if __name__ == '__main__':
    data = list(map(int, input().split()))

    res = PaperProblem(data)
    print(int(res))
