"""
title：列表基础语法
writer：山客
The_last_update_date：2021.9.8
"""

from collections import Counter


# 创建列表
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "a", "b", "c", "d"]
list3 = []  # 空数组

# 访问列表：索引（反向）、截取
print(list1[1:])
print(list2[2])
print(list2.index('c'))  # 根据值返回元素下标

# 更新列表：增删改
list1.append(6)  # 增加列表最后元素
print(list1)

list1.insert(2, -1)  # 插入列表任意位置元素
print(list1)

list2[3] = "e"
print(list2)

del list2[2]  # 删除任意位置元素
print(list2)

list2.pop()  # 删除列表最后元素
print(list2)

list2.remove('a')  # 删除列表第一个对应的元素
print(list2)

list2.extend(["a", "b", "c", "d"])  # 添加一个新序列，其实也可以直接用 +
print(list2)

# 内置函数
print(max(list1))  # min()
print(len(list1))
tup = ("a", 1, 2, "c")  # 转换列表
print(list(tup))
print(sorted(list1, reverse=True))  # 比较大小，默认reverse=false，升序
list1.reverse()  # 反转列表
print(list1)

# 统计列表
print(list2.count("a"))  # 统计单个元素出现的次数
print(Counter(list2))  # 统计所有元素出现的次数，返回dictionary



