"""
title：电路模拟
writer：山客
date：2021.9.18
key：电路实现
example：
输入：
6
A C E D B D
5
1 2 2 3 3 4 3 5 5 6
5
2 2 2 2 5
输出：
2 1
tips：
A：电源元件，0进1出；
B：额外电源元件，1进1出，只受不通电->通电影响；
C：开关，1进1出，单次点击状态改变并保持；
D：计数器，1进1出，脉冲信号 + 1，取模99；
E：分线器，1进4出；
"""


class Solution:
    def ArtificialCircuit(self, N: int, ID: list, NID: dict, M: int, Rs: dict, S: int, Ss: list):
        ress = {}  # 计数器结果
        STATEs = {}  # 元件当前状态

        for k, v in NID.items():
            if v == 'A':
                # 电源元件
                continue
            elif v == 'B':
                # 额外电源元件有 3 个状态
                # 0 - 初始； 1 - 通电 -> 不通电； 2 - 不通电 -> 通电
                STATEs[k] = 0
            elif v == 'D':
                # 计数器
                STATEs[k] = False
                ress[k] = 0
            else:
                # 开关与分线器元件
                STATEs[k] = False

        # 遍历每一次对开关进行的操作
        for s in Ss:
            # 点击在非开关上，无效
            if NID[s] != 'C':
                continue
            path = Rs[s].copy()

            STATEs[s] = not STATEs[s]  # 开关状态取反
            # 若开关按下后为正
            if STATEs[s]:
                while path:
                    # print('path : ', path)
                    node = path.pop(0)
                    # 额外电源元件
                    if NID[node] == 'B':
                        if STATEs[node] == 0:
                            # 不通电 -> 通电，正常工作
                            STATEs[node] = 2
                            # 路径更新
                            try:
                                path += list(Rs[node])
                            except:
                                pass
                        else:
                            # 若是不启动状态，则中断这一路
                            STATEs[node] -= 1
                            continue
                    # 开关元件
                    elif NID[node] == 'C':
                        # 若是断开的，则中断这一路，否则正常工作
                        if not STATEs[node]:
                            continue
                        else:
                            try:
                                path += list(Rs[node])
                            except:
                                pass
                    # 分线器 与 计数器
                    else:
                        STATEs[node] = STATEs[s]
                        # 路径更新
                        try:
                            path += list(Rs[node])
                        except:
                            pass

                    print('STATE : ', STATEs)

                    # 计数器操作
                    if NID[node] == 'D' and STATEs[node]:
                        ress[node] = (ress[node] + 1) % 99
                    print('RESS : ', ress)
            # 若为负
            else:
                while path:
                    node = path.pop(0)
                    # 额外电路元件
                    if NID[node] == 'B':
                        if STATEs[node] <= 2 and STATEs[node] > 0:
                            STATEs[node] -= 1
                    # 其他元件
                    else:
                        STATEs[node] = STATEs[s]

                    print('STATE : ', STATEs)

                    # 更新路径
                    try:
                        path += list(Rs[node])
                    except:
                        pass

        return ress


if __name__ == '__main__':
    N = int(input())  # N 个元件
    ID = list(input().split())  # N 个元件的 ID
    NID = {}
    for i in range(N):
        NID[i + 1] = ID[i]
    # print('元件：\n', NID)

    M = int(input())  # M 条电线
    Rs = {}  # 元件连接关系
    data = list(map(int, input().split()))
    for i in range(0, len(data) - 1, 2):
        if data[i] not in Rs:
            Rs[data[i]] = [data[i + 1]]
        else:
            Rs[data[i]].append(data[i + 1])
    # print('关系：\n', Rs)

    S = int(input())  # S 次点击开关操作
    Ss = list(map(int, input().split()))  # 点击开关操作

    s = Solution()
    ress = s.ArtificialCircuit(N, ID, NID, M, Rs, S, Ss)
    for res in ress.values():
        print(res, end=' ')
