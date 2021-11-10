"""
title：树上最短链
writer：山客
date：2021.8.15
key：DFS
example：
输入：
3
1 2 1
1 2
2 3
输出：
2
tips：
① 多注意跳出条件
"""

from collections import defaultdict


def ShortestChain(n: int, LEVEL: list, EDGES: list):
    # 确保有起码两座城市的等级一致，可以作为起点 / 终点
    l = defaultdict(list)
    for i in range(n):
        l[LEVEL[i]].append(i)
    if len(l) == n:
        return -1

    res = 1_000_000_007
    # 选取任意一个点为起点
    for k, v in l.items():
        # 确保有起码两座城市的等级一致，可以作为起点 / 终点
        if len(v) == 1:
            continue
        # 遍历所有点为起点
        # DFS
        for root in v:
            stack = [root]  # 保存深度搜索的顺序
            visited = set()  # 已经访问过的节点
            deep = 0
            # 遍历与起点关联的所有深度的所有点
            while stack:
                tmp = []
                # 遍历当前深度所有关联节点
                while stack:
                    node = stack.pop()
                    visited.add(node)
                    # 同等级，又不同点，可以当做起点 / 终点，遍历结束
                    if LEVEL[node] == LEVEL[root] and node != root:
                        res = min(res, deep)
                        break
                    # 整理当前点连接的其他所有点（已访问的除外）,准备下次遍历
                    for nxt in EDGES[node]:
                        if nxt not in visited:
                            tmp.append(nxt)
                # 下一层
                deep += 1
                stack = tmp.copy()
                # 如果当前层已经超过了目前的 res 层，则直接跳出循环
                if deep >= res:
                    break

    return res


if __name__ == '__main__':
    n = int(input())  # n 个城市
    LEVEL = list(map(int, input().split()))  # 每个城市的等级

    # 无向边
    EDGES = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        EDGES[x - 1].append(y - 1)
        EDGES[y - 1].append(x - 1)

    res = ShortestChain(n, LEVEL, EDGES)
    print(res)
