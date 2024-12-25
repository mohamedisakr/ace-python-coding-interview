# from collections import defaultdict
from typing import Optional, List


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def build_from_string_array(self, lines: List[str]):
        for line in lines:
            self.insert(line)


if __name__ == "__main__":
    content = ""

    with open('trie/wordsEn.txt', 'r') as file:
        content = file.read().splitlines()

    # print(type(content))

    trie = Trie()
    trie.build_from_string_array(content)
    print(trie)

    # """
    # trie.insert("apple")
    # print(trie.search("apple"))   # return True
    # print(trie.search("app"))     # return False
    # print(trie.startsWith("app"))  # return True
    # trie.insert("app")
    # print(trie.search("app"))     # return True
    # """

    # from pathlib import Path

    # file_path = Path('trie/wordsEn.txt')
    # content = file_path.read_text()
    # print(content)
