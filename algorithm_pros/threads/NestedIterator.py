"""
title: 扁平化嵌套列表迭代器
writer: 山客
date: 2021.3.23
example:
输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.lists = []
        self.index = 0

        def get_list(n: nestedList):
            for i in n:
                if i.isInteger():
                    # 判断是否为int型，如果是，就直接添加
                    self.lists.append(i.getInteger())
                else:
                    # 如果不是，那就对该处的list进行get_list操作，嵌套迭代。
                    get_list(i.getList())

        get_list(nestedList)

    def next(self) -> int:
        self.index += 1
        return self.lists[self.index - 1]

    def hasNext(self) -> bool:
        if self.index < len(self.lists):
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())