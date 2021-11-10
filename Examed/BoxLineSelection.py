"""
title：框线选段
writer：山客
date：2021.8.9
key：
example：
输入：
3 3 10 10
11 11 4 4
输出：
(10.00,10.00)
(4.00,4.00)
tips：
① 还无法处理贯穿纵横轴的点 L124 - 146
② 测试案例： 10 / 11
improvement：
①  用线段向量求解
"""


def BoxLineSelection(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int):
    origin = ()  # 起点
    destination = ()  # 终点

    # 如果线段在框内，则返回原始线段
    if x1 <= x3 <= x2 and y1 <= y3 <= y2 and \
        x1 <= x4 <= x2 and y1 <= y4 <= y2:
        origin = (x3, y3)
        destination = (x4, y4)
    # 线段有一部分在框内
    elif x1 <= x3 <= x2 and y1 <= y3 <= y2:
        origin = (x3, y3)  # 切线线段起点已知

        # 求终点
        try:
            k = (y4 - y3) / (x4 - x3)  # 线段系数 k
            b = y3 - k * x3  # 线段系数 b
        except:
            k = 0
            b = 0
        # print("x1 <= x3 <= x2 and y1 <= y3 <= y2", k, b)

        # 竖线
        if k == 0 and b == 0:
            if abs(y4 - y1) < abs(y4 - y2):
                destination = (x4, y1)
            else:
                destination = (x4, y2)
        # 横线
        elif k == 0:
            if abs(x4 - x1) < abs(x4 - x2):
                destination = (x1, y3)
            else:
                destination = (x2, y3)
        # 斜线
        else:
            if abs(x4**2 + y4**2 - x1**2 - y1**2) < abs(x4**2 + y4**2 - x2**2 - y2**2):
                tmp_y2 = y1
            else:
                tmp_y2 = y2

            tmp_x2 = (tmp_y2 - b) / k
            if x1 <= tmp_x2 <= x2:
                destination = (tmp_x2, tmp_y2)
    elif x1 <= x4 <= x2 and y1 <= y4 <= y2:
        destination = (x4, y4)  # 切线线段终点已知

        # 求起点
        try:
            k = (y4 - y3) / (x4 - x3)  # 线段系数 k
            b = y3 - k * x3  # 线段系数 b
        except:
            k = 0
            b = 0
        # print("x1 <= x4 <= x2 and y1 <= y4 <= y2", k, b)

        # 竖线
        if k == 0 and b == 0:
            if abs(y4 - y1) < abs(y4 - y2):
                origin = (x3, y1)
            else:
                origin = (x3, y2)
        # 横线
        elif k == 0:
            if abs(x3 - x1) < abs(x3 - x2):
                origin = (x1, y3)
            else:
                origin = (x2, y3)
        else:
            if abs(x3 ** 2 + y3 ** 2 - x1 ** 2 - y1 ** 2) < abs(x3 ** 2 + y3 ** 2 - x2 ** 2 - y2 ** 2):
                tmp_y1 = y1
            else:
                tmp_y1 = y2

            tmp_x1 = (tmp_y1 - b) / k
            if x1 <= tmp_x1 <= x2:
                origin = (tmp_x1, tmp_y1)
    # 线段未知与框的关系
    else:
        try:
            k = (y4 - y3) / (x4 - x3)  # 线段系数 k
            b = y3 - k * x3  # 线段系数 b
        except:
            k = 0
            b = 0
        print(k, b)

        # 竖线
        if k == 0 and b == 0:
            if abs(y3 - y1) < abs(y3 - y2):
                origin = (x3, y1)
                destination = (x3, y2)
            else:
                origin = (x3, y2)
                destination = (x3, y1)
        # 横线
        elif k == 0:
            if y1 <= y3 <= y2:
                if x3 < x1 and x4 > x2:
                    origin = (x1, y3)
                    destination = (x2, y3)
                elif x4 < x1 and x3 > x2:
                    origin = (x2, y3)
                    destination = (x1, y3)
        else:
            # 通过 y = kx + b 计算当y轴确定时，x的位置
            tmp_y1 = y1
            tmp_x1 = (tmp_y1 - b) / k
            tmp_y2 = y2
            tmp_x2 = (tmp_y2 - b) / k

            # 证明原始线段与矩形有切线
            if x1 <= tmp_x1 <= x2 and x1 <= tmp_x2 <= x2 and \
                    x3 <= tmp_x1 <= x4 and x3 <= tmp_x2 <= x4:
                # 距离线段起点小的为切线起点
                tmp_ori = min(abs(tmp_x1 ** 2 + tmp_y1 ** 2 - x3 ** 2 - y3 ** 2),
                              abs(tmp_x2 ** 2 + tmp_y2 ** 2 - x3 ** 2 - y3 ** 2))
                if tmp_ori == abs(tmp_x1 ** 2 + tmp_y1 ** 2 - x3 ** 2 - y3 ** 2):
                    origin = (tmp_x1, tmp_y1)
                    destination = (tmp_x2, tmp_y2)
                else:
                    origin = (tmp_x2, tmp_y2)
                    destination = (tmp_x1, tmp_y1)

    if origin and destination:
        return origin, destination
    else:
        return -1


if __name__ == '__main__':

    x1, y1, x2, y2 = input().split()  # 矩形左下、右上坐标
    x3, y3, x4, y4 = input().split()  # 线段起点、终点坐标

    res = BoxLineSelection(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3), int(x4), int(y4))

    if res != -1:
        print('(' + '%.2f'%res[0][0] + ',%.2f'%res[0][1] + ')')
        print('(' + '%.2f' %res[1][0] + ',%.2f' %res[1][1] + ')')
    else:
        print(-1)
