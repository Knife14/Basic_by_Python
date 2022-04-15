"""
title：常见基础语法
writer：山客
The_last_update_date：2021.5.20
"""

from collections import Counter  # 统计
import wordcloud  # 中文词云

from sortedcontainers import SortedSet

import socket  # 套接字
import socketserver

import itertools  # 排列组合

# 有序去重集合
'''
  input: list, str
  output: SortedSet[]
  tips: list(output)
'''
tmp = ['a', 'a', 'b', 'c', 'd', 'd', 'd', 'e']
s = SortedSet(tmp)
print(list(s))

# 遍历数据对象组合为索引序列
BV_ID = "BV11E411n7D6"
print(list(enumerate(BV_ID)))

# 输入
i1, i2, i3 =input(".split()接收多个用户输入，空格相间，回车结束：\n").split()
print(i1, i2, i3)
print(i1, type(i1), len(i1))

# 打印print
a = ['1', '2', '3']
b = ['2', '4', '6']

print('a = {0} \nb = {1}'.format(a, b))  # ,format()的运用
print("".join(a[i] + b[i] for i in range(len(a))))  # 数组（元素需要是字符串）打印成字符串

# int进制类型转换 int(object, base=2 / 8 / 10 / 16...)
# 转换为二进制形式的int型，然后相加
print('{0:b}'.format(int('10', 2) + int('01', 2)))