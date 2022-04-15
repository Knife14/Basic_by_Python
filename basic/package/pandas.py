"""
Package：pandas
writer：山客
The_last_update_date：2021.4.27
usage：数据分析
data structure：
① Series：一维数组。
② Time- Series：以时间为索引的Series。
③ DataFrame：二维的表格型数据结构。
④ Panel：三维的数组。
⑤ PanelND：N维命名容器的模块。
"""

import pandas

# 二维字典转矩阵
graph = {
    'a': {'b': 7, 'c': 9, 'f': 14},
    'b': {'a': 7, 'c': 10, 'd': 15},
    'c': {'a': 9, 'b': 10, 'd': 11, 'f': 2},
    'd': {'b': 15, 'c': 11, 'e': 6},
    'e': {'d': 6, 'f': 9},
    'f': {'a': 14, 'c': 2, 'e': 9}
}
map = pandas.DataFrame(graph).T.fillna(1_000_000_007)  # 空的地方置 1_000_000_007

for index in map.iterrows():
    # 按行遍历
    print(index)

for index, row in map.iterrows():
    # 按行遍历
    # 输出每一行的索引 - index
    # 输出每一行对应列元素 - row[i]
    print(index, row[0])

for row in map.iteritems():
    # 按列遍历
    print(row)

for index, row in map.iteritems():
    # 按列遍历
    # 输出每一列的索引 - index
    # 输出对应行的每一列元素 - row
    print(index, row[1])
