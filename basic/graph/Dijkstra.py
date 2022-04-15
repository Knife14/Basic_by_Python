"""
title：Dijkstra - 迪科斯彻算法
writer：山客
date：2021.7.31
thinking：
①需要计算非负权有向图G中的最短路径，指定起点s
②引进集合S、U，S记录已求出最短路径的顶点，U记录还未求出最短路径的顶点
③从U中找出路径最短的顶点，并加入到S中
④重复③，直至遍历完所有顶点
tips：
①广度优先搜索
②松弛操作
③贪心算法 + 回溯
④先将地图字典存为二维数组，方便后续进行松弛等操作
improvement：
①输入简洁化，处理重构化：ascii码？输入类型函数重构？ pandas遍历？
②路径输出
return:
①该顶点到各个顶点的最短距离
"""

mod = 1_000_000_007


def Dijkstra(map: list, begin: str):
    # init - 初始化
    vertex, num = -1, len(map)
    path, distance = [], [mod] * num
    visited = set()

    distance[int(begin) - 1] = 0

    # Dijkstra
    for i in range(0, num):
        min = mod

        # 查找当前distance权值最小的点，作为新的起始点
        for j in range(0, num):
            if j not in visited and distance[j] < min:
                min = distance[j]
                vertex = j
        # 若没查找到或已经查找完毕，返回
        if min == mod:
            return

        visited.add(vertex)
        path.append(str(vertex + 1))

        # 松弛操作 distance[j] > distance[vertex] + map[vertex][j]
        for j in range(0, num):
            if j not in visited and \
                    distance[j] > distance[vertex] + map[vertex][j]:
                distance[j] = distance[vertex] + map[vertex][j]
                # path[j].append(j)

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
    print(Dijkstra(map, '6'))
