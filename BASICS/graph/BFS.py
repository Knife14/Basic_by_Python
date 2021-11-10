"""
title：广度优先搜索
writer：山客
date：2021.4.26
thinking：
①假设当前所有顶点都未被访问
②选定一个顶点，并且将这个顶点设置为已经访问过的顶点
③搜索该顶点的所有邻接节点，若邻接点存在，则重复②③
"""


def BFS(graph: dict, begin) -> list:

    stack, visited = [], []

    # 用栈来保存深度搜索的顺序，visited保存已访问节点
    stack.append(begin)
    visited.append(begin)

    while len(stack) > 0:
        # 保存第一个节点并弹出，方便其下面的子节点接入
        vertex = stack.pop(0)
        # 子节点的邻接节点
        nodes = graph[vertex]
        for node in nodes:
            if node not in visited:
                visited.append(node)
                stack.append(node)

    return visited


if __name__ == '__main__':
    graph1 = {
        1: [3], 2: [4],
        3: [4, 5], 4: [2, 3, 5, 6],
        5: [3, 4], 6: [4]
    }

    graph2 = {
        'A': ['C'], 'B': ['D'],
        'C': ['D', 'E'], 'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'], 'F': ['D']
    }

    print(BFS(graph1, begin=1))
    print(BFS(graph2, begin='A'))
