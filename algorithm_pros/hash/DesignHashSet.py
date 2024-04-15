"""
title: 设计哈希集合
writer: m14
date: 2024.4.15
key：哈希映射，插入删除时间复杂度应为O(1)
example:
输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]
解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
thinking：时间复杂度O(n/b)，空间复杂度O(n)
"""


class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.set = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.set[hashkey]:
            return False
        
        self.set[hashkey].append(key)
        return True

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.set[hashkey]:
            self.set[hashkey].remove(key)
            return True

        return False

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        return key in self.set[hashkey]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
