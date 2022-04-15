"""
title：对称飞行器
writer：山客
date：2021.8.15
key：
example：
输入：
4 4
#S..
E#..
#...
....
输出：
4
tips：
① 注意队列的使用，需要引入deque包，如果直接用list，会超时
② queue - deque；visited - set
"""
from collections import deque

isSuccess = False


def SymAircaft(n: int, m: int, dmap: list):
    times = 0  # 耗费时间
    global isSuccess

    # 记录飞行器、结束的坐标
    curr = ((0, 0), 0)  # 坐标 + 剩余飞行次数
    E = (0, 0)

    # 不使用飞行器，普通移动
    def MOVE(curr: tuple, dire: tuple):
        (x, y), times = curr
        dx, dy = dire
        return (x + dx, y + dy), times

    # 使用飞行器，飞行规则： x + x′= n + 1且 y + y′= m + 1
    def SYMFLY(curr: tuple):
        (x, y), times = curr
        return (n - 1 - x, m - 1 - y), times - 1

    # 检查越界等条件
    def CHECK(curr: tuple):
        (x, y), times = curr
        return (
            0 <= x < m
            and 0 <= y < n
            and times >= 0   # 飞行器剩余次数
            and dmap[x][y] != '#'  # 前往格子不是障碍物
            and (x, y) not in visited  # 已经遍历过的节点
        )

    for i in range(n):
        for j in range(m):
            if dmap[i][j] == 'S':
                curr = ((i, j), 5)
            if dmap[i][j] == 'E':
                E = (i, j)
    # print(curr, E)

    # 用队列来保存搜索的顺序，visited保存已访问节点
    queue = deque([curr])
    visited = set(curr[0])

    # 可移动方向
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS
    while queue:
        # 针对当前结点，遍历 所有 附近结点，得到当前情况下的所有可能
        # 无论使用飞行器与否，每次移动时间成本 + 1
        for _ in range(len(queue)):
            tmp = queue.popleft()
            # 如果已经到达终点
            if tmp[0] == E:
                isSuccess = True
                return times
            # 普通移动
            for dire in directions:
                dtmp = MOVE(tmp, dire)
                if CHECK(dtmp):
                    visited.add(dtmp[0])
                    queue.append(dtmp)
            # 对称飞行
            ftmp = SYMFLY(tmp)
            if CHECK(ftmp):
                visited.add(ftmp[0])
                queue.append(ftmp)

        # 遍历结束，时间成本 + 1
        times += 1


if __name__ == '__main__':
    n, m = map(int, input().split())  # 迷宫 n 行 m 列
    dmap = [input() for _ in range(n)]  # 迷宫

    res = SymAircaft(n, m, dmap)

    if isSuccess:
        print(res)
    else:
        print(-1)
