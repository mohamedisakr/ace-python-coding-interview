# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

# from collections import defaultdict
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # return True
    print(trie.search("app"))     # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))     # return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # return True
    print(trie.search("app"))     # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))     # return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)  # {}
#         self.is_end_of_word = False

# class TrieNode:
#     def __init__(self):
#         self.children: dict[str, TrieNode] = {}
#         self.is_end_of_word: bool = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         node: TrieNode = self.root
#         for char in word:
#             node = node.children.setdefault(char, TrieNode())
#         node.is_end_of_word = True

#     def search(self, word: str) -> bool:
#         node: TrieNode = self._find(word)
#         return node and node.is_end_of_word

#     def startsWith(self, prefix: str) -> bool:
#         return self._find(prefix)

#     def _find(self, prefix: str) -> TrieNode | None:
#         node: TrieNode = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return None
#         node = node.children[char]
#         return node

# ===========

# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.is_end_of_word = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word:
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.is_end_of_word

#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
