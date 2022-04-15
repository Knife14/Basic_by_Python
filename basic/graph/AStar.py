"""
title：A* AStar.py
writer：山客
date：2021.8.2
thinking：
①首先将起始节点S放入OPEN表，CLOSE表置空
②如果OPEN表不为空，从表头取一个结点n，如果为空算法失败
③n是目标解吗？是，找到一个解，并且继续或者终止算法
④将n的所有后继节点展开，就是从n可以直接关联的子节点，
  如果不在CLOSE表中，就将他们加入OPEN表中，并把S放入CLOSE表，
  同时计算每一个后继结点的估价值f(n)，将OPEN表按f(x)排序，
  最小的放表头，重复算法②③④
tips：
① F = G + H
   G = 移动代价 * 代价因子
improvement：
①选择排序更快的二叉树来作为OPEN表（该代码中所使用的是遍历求取）
②考虑直线通行的可能性，可以采用 兰森汉姆 算法
③A*算法得出路径后，可采用 弗洛伊德 算法对路径进行平滑处理 
return:
a new MAP
"""

# coding=utf-8

# 节点坐标数据
class POINT:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 节点
class NODE:
    def __init__(self, point: 'POINT', G=0, H=0):
        self.point = point  # 坐标数据
        self.father = None  # 父节点
        self.G = G          # 开始点到当前格的移动代价
        self.H = H          # 当前格到结束格的预估移动代价

    def SetH(self, endNode: 'NODE'):
        # 估算预估代价H
        # 曼哈顿算法
        self.H = (
            abs(endNode.point.x - self.point.x) + abs(endNode.point.y - self.point.y)
        ) * 10

    def SetG(self, G):
        # 设置当前移动代价G
        self.G = G

    def SetFather(self, FatherNode: 'NODE'):
        # 设置当前节点的父节点
        self.father = FatherNode

# 地图
class MAP:
    def __init__(self, data: list, weight: int, height: int):
        # 初始化
        self.data = data      # 地图数据
        self.weight = weight  # 地图宽度
        self.height = height  # 地图高度
        self.passTag = '.'    # 地图格可通行标志
        self.pathTag = '*'    # 地图格已通过标志

    def ShowMap(self):
        # 展示地图
        for x in range(self.height):
            for y in range(self.weight):
                print(self.data[x][y],end=' ')
            print('\n')

    def SetMap(self, point: 'POINT'):
        # 修改地图格信息
        # 若经过这个地图格，则将地图格信息修改为 '*'
        self.data[point.x][point.y] = self.pathTag

    def IsPass(self, point: 'POINT') -> bool:
        # 判断地图格情况
        if (point.x < 0 or point.x > self.height - 1) or \
            (point.y < 0 or point.y > self.weight -1):
            # 越界
            return False

        if self.data[point.x][point.y] == self.passTag:
            # 如果地图格是可通行的，则返回 True
            return True

# A*算法
class AStar:
    def __init__(self, map: 'MAP', StartNode: 'NODE', EndNode: 'NODE'):
        """
        :title: 初始化
        :param map: 地图数组
        :param StartNode: 寻路起点
        :param EndNode: 寻路终点
        """
        self.OPEN = []                # 开放列表
        self.CLOSE = []               # 封闭列表
        self.MAP = map                # 地图数据
        self.STARTNODE = StartNode    # 起点
        self.ENDNODE = EndNode        # 终点
        self.CURRENTNODE = StartNode  # 当前处理的节点
        self.PATH = []                # 生成路径

    def FindMinFNode(self) -> 'NODE':
        # 获得OPEN表中 F 值最小的节点

        tmp = self.OPEN[0]  # 取OPEN表中任意一个节点
        for node in self.OPEN:
            if node.G + node.H < tmp.G + tmp.H:
                # 若计算代价比原先点小，则保留该点
                tmp = node

        # 返回OPEN表估价值最小的点
        return tmp

    def IsNodeInOpenList(self, node: 'NODE') -> bool:
        # 判断节点是否在OPEN表中

        # 是
        for tmp in self.OPEN:
            if tmp.point.x == node.point.x and \
                tmp.point.y == node.point.y:
                return True

        # 否
        return False

    def IsNodeInCloseList(self, node: 'NODE') -> bool:
        # 判断节点是否在CLOSE表中

        # 是
        for tmp in self.CLOSE:
            if tmp.point.x == node.point.x and \
                tmp.point.y == node.point.y:
                return True

        # 否
        return False

    def IsEndNodeInOpenList(self):
        # 判断终点是否在OPEN表中

        # 是
        for tmp in self.OPEN:
            if tmp.point.x == self.ENDNODE.point.x and \
                tmp.point.y == self.ENDNODE.point.y:
                return True

        # 否
        return False

    def GetNodeFromOPEN(self, node: 'NODE'):
        # 从OPEN表中取节点
        for tmp in self.OPEN:
            if tmp.point.x == node.point.x and \
                tmp.point.y == node.point.y:
                return tmp

        return None

    def Search(self, node: 'NODE'):
        # 搜索节点，并对该节点进行分析处理

        # 忽略障碍
        if self.MAP.IsPass(node.point) != True:
            return

        # 忽略封闭(CLOSE)列表
        if self.IsNodeInCloseList(node):
            return

        # 计算 G， 斜向的 G 为 14， 正向的 G 为 10
        if abs(node.point.x - self.CURRENTNODE.point.x) == 1 and \
            abs(node.point.y - self.CURRENTNODE.point.y) == 1:
            G_tmp = 14
        else:
            G_tmp = 10

        # 若关联节点不在OPEN表中，将当前节点的关联节点加入到OPEN表中
        if self.IsNodeInOpenList(node) != True:
            node.SetG(G_tmp)
            node.SetH(self.ENDNODE)  # 计算 H
            self.OPEN.append(node)   # 加入OPEN表
            node.father = self.CURRENTNODE  # 设置父节点
        else:
            # 如果节点已经在OPEN表中，判断CURRENT到当前点的 G 是否更小
            tmp = self.GetNodeFromOPEN(node)
            if self.CURRENTNODE.G + G_tmp < tmp.G:
                tmp.G = self.CURRENTNODE.G + G_tmp
                tmp.father = self.CURRENTNODE

    def SearchNear(self):
        # 搜索当前节点附近的点
        # 一共八个方向，分别是：左上、上、右上；左、右；左下、下、右下；
        # 拐角无法直接到达

        # 左上
        if self.MAP.IsPass(POINT(self.CURRENTNODE.point.x - 1, self.CURRENTNODE.point.y)) and \
            self.MAP.IsPass(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y - 1)):
            self.Search(NODE(POINT(self.CURRENTNODE.point.x - 1, self.CURRENTNODE.point.y - 1)))

        # 上
        self.Search(NODE(POINT(self.CURRENTNODE.point.x - 1, self.CURRENTNODE.point.y)))

        # 右上
        if self.MAP.IsPass(POINT(self.CURRENTNODE.point.x - 1, self.CURRENTNODE.point.y)) and \
            self.MAP.IsPass(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y + 1)):
            self.Search(NODE(POINT(self.CURRENTNODE.point.x - 1, self.CURRENTNODE.point.y + 1)))

        # 左、右
        self.Search(NODE(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y - 1)))
        self.Search(NODE(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y + 1)))

        # 左下
        if self.MAP.IsPass(POINT(self.CURRENTNODE.point.x + 1, self.CURRENTNODE.point.y)) and \
            self.MAP.IsPass(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y - 1)):
            self.Search(NODE(POINT(self.CURRENTNODE.point.x + 1, self.CURRENTNODE.point.y - 1)))

        # 下
        self.Search(NODE(POINT(self.CURRENTNODE.point.x + 1, self.CURRENTNODE.point.y)))

        # 右下
        if self.MAP.IsPass(POINT(self.CURRENTNODE.point.x + 1, self.CURRENTNODE.point.y)) and \
            self.MAP.IsPass(POINT(self.CURRENTNODE.point.x, self.CURRENTNODE.point.y + 1)):
            self.Search(NODE(POINT(self.CURRENTNODE.point.x + 1, self.CURRENTNODE.point.y + 1)))

    def Start(self):
        # 开始寻路

        # 将初始节点放入OPEN表中
        self.STARTNODE.SetH(self.ENDNODE)  # 设置初始节点的 H
        self.STARTNODE.SetG(0)             # 设置初始节点的 G
        self.OPEN.append(self.STARTNODE)

        while True:
            # 获取当前OPEN表里 F 值最小的节点，并将其在OPEN表中删除，加入CLOSE表
            self.CURRENTNODE = self.FindMinFNode()
            self.CLOSE.append(self.CURRENTNODE)
            self.OPEN.remove(self.CURRENTNODE)

            self.SearchNear()

            # 通过判断EndNode是否在OPEN表中，检验是否结束
            # 是
            if self.IsEndNodeInOpenList():
                tmp = self.GetNodeFromOPEN(self.ENDNODE)
                while True:
                    self.PATH.append(tmp)
                    if tmp.father != None:
                        tmp = tmp.father
                    else:
                        return True
            # 否，且OPEN表已经空了，算法结束，寻路失败
            elif len(self.OPEN) == 0:
                return False

    def SetMap(self):
        # 修改地图信息
        # 已经经过的节点，更改为 '*'
        for node in self.PATH:
            self.MAP.SetMap(node.point)


if __name__ == '__main__':
    # 构建地图
    map_data = [
        list("####################"),
        list("#.....#............#"),
        list("#.....#.....#.####.#"),
        list("#.########.##......#"),
        list("#.....#.....######.#"),
        list("#.....#####.#......#"),
        list("####..#.....#.######"),
        list("#.....#..#..#..#...#"),
        list("#..#.....#..#....#.#"),
        list("####################")
    ]
    test = MAP(map_data, 20, 10)
    print("原始地图：")
    test.ShowMap()

    # 构建 A*
    start = NODE(POINT(1, 1))
    end = NODE(POINT(8, 18))
    AS = AStar(test, start, end)

    # 开始寻路
    if AS.Start():
        AS.SetMap()     # 修改地图信息
        print("寻路后：")
        test.ShowMap()
    else:
        print(-1)
