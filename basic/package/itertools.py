"""
Package：itertools
writer：山客
The_last_update_date：2021.4.27
usage：排列组合常用工具
data structure：数组 / 字符串
"""

import itertools

a = "122"
res_A = itertools.permutations(a)  # 排列
res_C = itertools.combinations(a, 2)  # 组合 C(len(a))n

print(list(res_A))
print(list(res_C))