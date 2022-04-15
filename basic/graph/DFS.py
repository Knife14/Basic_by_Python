"""
title：深度优先搜索
writer：山客
date：2021.4.6
thinking：
①假设当前所有顶点都未被访问
②选定一个顶点，并且将这个顶点设置为已经访问过的顶点
③搜索该顶点的邻接节点，若邻接点存在，则重复②③
tips：
①引入栈，栈保存深度搜索的返回顺序
②需要回溯，当该邻接节点不能再继续的时候
③回溯利用栈保存的顺序
improving：
① stack 换成队列， visited 换成 set() 可以有效提高效率
"""


def DFS(graph: dict, begin) -> list:

    stack, visited = [], []

    # 用栈来保存深度搜索的顺序，visited保存已访问节点
    stack.append(begin)
    visited.append(begin)

    while len(stack) > 0:
        # 找到当前节点的所有邻接点
        index = stack.pop()
        nodes = graph[index]  # type(nodes) = list

        for i in nodes:
            if i not in visited:
                # 标记为访问节点
                stack.append(i)
                visited.append(i)

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

    print(DFS(graph1, begin=1))
    print(DFS(graph2, begin='A'))
