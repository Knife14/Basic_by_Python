"""
Package：numpy
writer：山客
The_last_update_date：2021.5.10
usage：处理数组
data structure：数组
"""

import numpy

# 快速创建升序数组
a = numpy.arange(0, 8, 1)   # start, end, step(int/float)

# 不改变数据的情况下修改形状
b = a.reshape(2, 4)  # lines, columns
print('原始数组：\n', b)

# 数组单个元素迭代器
print('迭代数组元素：')
for i in b.flat:
    print(i, end=' ')
print('')

# 数组单组元素迭代
# numpy.ravel 类似于 numpy.ndarray.flatten
print('迭代数组：\n', b.flatten(order='F'))  # C - 按行；F - 按列；A - 原顺序； K - 按内存顺序

# 正无穷，负无穷 -inf
print(numpy.inf)
# 不是数字
print(numpy.nan)
print(numpy.nan != numpy.nan)
