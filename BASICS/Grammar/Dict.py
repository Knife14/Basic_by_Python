"""
title：字典基础语法
writer：山客
The_last_update_date：2021.4.26
"""

s = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

# 更新字典
s['a'] = 0  # 修改
s['e'] = 5  # 添加
print(s)
del s['e']  # 删除  && dict.clear() - 清空字典  && del dict 删除字典
print(s)

# 遍历
'''
.items() - 以列表返回可遍历的(键, 值) 元组数组
.keys() - 以列表返回一个字典所有的键
.values() - 以列表返回字典中的所有值
'''
for k, v in s.items():
    print(k, v)

# 按照key值排序
print(sorted(s.items()))

# 按照value值排序
# x[1]为下标，若x[0]即为按照key值排序
# reverse : True - 降序 ， False - 升序，默认升序
print(sorted(s.items(), key=lambda x: x[1], reverse=False))

# 元组排序，默认降序
# zip() - 将对象中对应元素打包成一个个元组再存入数组中
f = zip(s.keys(), s.values())
print(sorted(f))

# 内置函数
print(len(s))  # 返回键数
print(s.pop('a'))  # 删除对应key的value
print(s.popitem())  # 删除最后的键值对
print(s.get('b'))  # 返回对应键值
try:
    # 如果键不存在于字典中，将会添加键并将值设为None
    print(s.setdefault('a'))
except:
    print("Wrong!")
# .fromkeys() - 快捷创建新字典
tmp = dict.fromkeys(['Google', 'Runoob', 'Taobao'], 'Emmm...')
print(tmp)
# .update() - 字典dict2的键值对添加到dict1里，若有重复键，则dict2的键值对更新dict1
s.update(tmp)
print(s)


