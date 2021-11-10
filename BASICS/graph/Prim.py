"""
title：Prim
writer：山客
date：2021.7.31
thinking：
①在一个加权连通图中，顶点集合V，边集合为E
②任意选出一个点作为初始顶点，标记为visited，计算所有与之相连接的点的距离，
  选择距离最短的点，标记visited
③在剩下的点，计算与已标记visited点距离最小的点，标记为visited
tips：
暂无
improvement：
暂无
"""

mod = 1_000_000_007


def Prim(map: list, begin: str):
    # init - 初始化
    vertex, num = -1, len(map)
    path, distance = [], [mod] * num

    visited = set()
    visited.add(int(begin) - 1)

    en = 0  # 连通标志

    # 计算所有与之相连接的点的距离
    for i in range(num):
        distance[i] = map[int(begin) - 1][i]

    for i in range(num - 1):
        min = mod

        # 选出最短距离的点
        for j in range(num):
            if min > distance[j] and j not in visited:
                min = distance[j]
                en = j

        # 标记最短距离的点为visited
        visited.add(en)
        path.append(str(en + 1))

        # 松弛操作
        for j in range(num):
            if distance[j] > map[en][j] and j not in visited:
                distance[j] = map[en][j]
                # path[j].append(en)

    return path, distance


if __name__ == '__main__':
    graph = {
        '1': {'2': 7, '3': 9, '6': 14},
        '2': {'1': 7, '3': 10, '4': 15},
        '3': {'1': 9, '2': 10, '4': 11, '5': 2},
        '4': {'2': 15, '3': 11, '5': 6},
        '5': {'4': 6, '6': 9},
        '6': {'1': 14, '3': 2, '5': 9}
    }
    map = [
        [0, 7, 9, mod, mod, 14],
        [7, 0, 10, 15, mod, mod],
        [9, 10, 0, 11, 2, mod],
        [mod, 15, 11, 0, 6, mod],
        [mod, mod, mod, 6, 0, 9],
        [14, mod, 2, mod, 9, 0]
    ]
    print(Prim(map, '6'))
