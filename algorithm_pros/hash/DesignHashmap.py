"""
title: 设计哈希映射
writer: m14
date: 2024.4.15
key：哈希映射，插入删除时间复杂度应为O(1)
example:
输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
thinking：时间复杂度O(n/b)，空间复杂度O(n)
"""


class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.map = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def put(self, key: int, value: int) -> None:
        hashkey = self.hash(key)
        for item in self.map[hashkey]:
            if item[0] == key:
                item[1] = value
                return 1
        self.map[hashkey].append([key, value]) 
        return 1

    def get(self, key: int) -> int:
        hashkey = self.hash(key)
        for item in self.map[hashkey]:
            if item[0] == key:
                return item[1]
        
        return -1

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        for idx, item in enumerate(self.map[hashkey]):
            if item[0] == key:
                self.map[hashkey].pop(idx)
                return 1
        
        return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
