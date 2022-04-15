"""
title：元组基础语法
writer：山客
The_last_update_date：2021.4.24
key：元组类似数组，但元组内的元素不能修改
"""

# 创建元组
tup1 = (1, 2, 3, 4, 5)
tup2 = ("a", "b", "c", "d")

tup3 = ()  # 空元组
tup4 = ("one",)  # 元组只有一个元素时

# 访问元组：索引（反向）、截取
print(tup1[2])
print(tup1[1:])

# 连接元组
print(tup1 + tup4)

# 删除元组
del tup1
try:
    print(tup1)
except:
    print("Deleted !")

# 内置函数
print(len(tup2))
print(max(tup2))  # min()

s = [1, 2, 3]  # 转换元组
print(tuple(s))

# 比较大小
tup1 = (1, 2, 3, 4, 5)
# return bool，一般返回元组第一位元素的比较结果
# 若元组前边元素均相等，则元组长度长的为大
print(tup1 > tuple(s))