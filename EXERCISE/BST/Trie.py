"""
title: 实现Trie（前缀树）
writer: 山客
date: 2021.4.14
Key：字典树=前缀树
problem：
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
tips：
① 字典树保存的是小写英文字母的数量
② ord() 函数返回的是字符的ASCII对应编号
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 字典树保存的是小写英文字母的数量
        self.children = [None] * 26
        # 字符串的结尾状态
        self.isEnd = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            char = ord(char) - ord("a")
            if not node.children[char]:
                # 如果该位置是空的，就需要新建节点
                node.children[char] = Trie()
            node = node.children[char]

        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def searchPrefix(self, prefix: str):
        node = self
        for char in prefix:
            char = ord(char) - ord("a")
            if not node.children[char]:
                return None
            node = node.children[char]

        return node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None


if __name__ == '__main__':
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
