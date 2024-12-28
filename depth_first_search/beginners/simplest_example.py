from typing import Optional, Tuple, Type, Any
from tree_node import TreeNode


class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation.
    """

    def __init__(self):
        self._root: TreeNode = None

    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'

    def __str__(self) -> str:
        return TreeNode._node_str(self._root)

    def contains(self, val: int) -> Optional[Tuple[TreeNode, TreeNode]]:
        return self._search(val)

    def _search(self, val: int) -> Optional[Tuple[TreeNode, TreeNode]]:
        parent: TreeNode = None
        current: TreeNode = self._root

        while current:
            if current.value() == val:
                return current, parent
            elif current.value() < val:
                parent = current
                current = current.left()
            else:
                parent = current
                current = current.right()

        return None, None
