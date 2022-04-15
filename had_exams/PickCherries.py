"""
title：树上摘樱桃
writer：山客
date：2021.8.21
key：
example：
输入：
10 9
1 left 2
1 right 3
2 left 4
2 right 5
3 right 6
6 left 7
6 right 8
8 left 9
8 right 10
输出：
2
tips：
"""


def PickCherries(m: int, n: int, data: list):
    # 整理树结构
    cnt = {}
    for i in range(n):
        if data[i][0] not in cnt:
            cnt[data[i][0]] = list(data[i][2])
        else:
            cnt[data[i][0]].append(data[i][2])

    # 遍历所有树结构
    res = 0
    for k, v in cnt.items():
        isLeaf = False  # 是否为樱桃节点
        if len(v) <= 1:
            continue
        else:
            for i in v:
                # 若子节点都不作为另一树结构的根节点，则为樱桃节点
                if i not in cnt:
                    isLeaf = True
                # 否则为false，并且直接跳出该次遍历
                else:
                    isLeaf = False
                    break
            if isLeaf == True:
                res += 1

    return res


if __name__ == '__main__':
    m, n = input().split()
    m, n = int(m), int(n)  # 节点数 m ， 边数 n

    data = []
    for _ in range(n):
        data.append(list(input().split()))

    res = PickCherries(m, n, data)
    print(res)
