from typing import Dict, Optional, List, Tuple
from node import TreeNode


class BinaryTree:
    def __init__(self) -> None:
        self._root: Optional[TreeNode] = None
        self._nodes: Dict[int, TreeNode] = {}

    def inorder(self) -> None:
        def _inorder(node: Optional[TreeNode]) -> None:
            if node:
                _inorder(node.left)
                print(f"({node.index}) {node.key}")
                _inorder(node.right)

        if self._root:
            _inorder(self._root)

    def populate_tree(self, data: List[Tuple[int, int, Optional[int], Optional[int]]]) -> None:
        for index, key, left, right in data:
            if index not in self._nodes:
                self._nodes[index] = TreeNode(key, index)
            node = self._nodes[index]

            if left is not None:
                if left not in self._nodes:
                    self._nodes[left] = TreeNode(None, left)
                node.left = self._nodes[left]
                node.left.val = data[left - 1][1]

            if right is not None:
                if right not in self._nodes:
                    self._nodes[right] = TreeNode(None, right)
                node.right = self._nodes[right]
                node.right.val = data[right - 1][1]

        self._root = self._nodes[6]  # Assuming the root is at index 6

    def draw_tree(self) -> None:
        pass


# Data in the format (index, key, left, right)
data: List[Tuple[int, int, Optional[int], Optional[int]]] = [
    (1, 17, 8, 9),
    (2, 14, None, None),
    (3, 12, None, None),
    (4, 20, 10, None),
    (5, 33, 2, None),
    (6, 15, 1, 4),
    (7, 28, None, None),
    (8, 22, None, None),
    (9, 13, 3, 7),
    (10, 25, None, 5)
]

# Creating the binary tree
binary_tree = BinaryTree()

# Populating the binary tree with data
binary_tree.populate_tree(data)

print("Inorder traversal of the binary tree with indices is:")
binary_tree.inorder()
