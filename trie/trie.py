# from collections import defaultdict
from typing import Optional, List


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word = False
        # self.children: Optional[dict[str, TrieNode]] = None

    """
    # def add_child(self, char: str) -> 'TrieNode':
    #     if self.children is None:
    #         self.children = {}
    #     if char not in self.children:
    #         self.children[char] = TrieNode()
    #     return self.children[char]
    """


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def search(self, word: str) -> bool:
        current = self._find_node(word)
        return current is not None and current.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def build_from_string_array(self, lines: List[str]):
        for line in lines:
            self.insert(line)

    def visualize(self) -> None:
        def _visualize(node: TrieNode, indent: str) -> None:
            for char, child in node.children.items():
                print(f"{indent}{char}")
                _visualize(child, indent + " ")

            if node.is_word:
                print(f"{indent}(word)")

        _visualize(self.root, "")


if __name__ == "__main__":
    content = ""

    with open('trie/wordsEn.txt', 'r') as file:
        content = file.read().splitlines()

    trie = Trie()
    trie.build_from_string_array(content)
    trie.visualize()

    # print(type(content))

    # words = ["apple", "app", "banana", "band", "bandana"]
    # trie.build_from_string_array(words)

# def insert(self, word: str) -> None:
#     node = self.root
#     for char in word:
#         node = node.add_child(char)
#     node.is_word = True
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
