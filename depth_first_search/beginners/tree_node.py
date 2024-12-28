from typing import Optional, Tuple, Type, Any


class TreeNode:
    """A class modeling the nodes of the binary search tree."""

    def __init__(self, value: Any, left: Type['TreeNode'] = None, right: Type['TreeNode'] = None):
        self._value = value
        self._left = left
        self._right = right

    def left(self) -> Type['TreeNode']:
        """Return a reference to the left child of the node."""
        return self._left

    def right(self) -> Type['TreeNode']:
        """Return a reference to the right child of the node."""
        return self._right

    def value(self) -> Any:
        """Return the value of the node."""
        return self._value

    def set_left(self, node: Type['TreeNode']) -> None:
        """Set the left child of the node. The old value will be lost."""
        self._left = node

    def set_right(self, node: Type['TreeNode']) -> None:
        """Set the right child of the node. The old value will be lost."""
        self._right = node

    @staticmethod
    def _node_str(node: Type['TreeNode']) -> str:
        return str(node) if node is not None else ''

    def __str__(self) -> str:
        left_str = TreeNode._node_str(self._left)
        right_str = TreeNode._node_str(self._right)
        return f'{self._value} ({left_str})({right_str})'

    def find_min_in_subtree(self) -> Tuple[Type['TreeNode'], Type['TreeNode']]:
        """Return the node with the smallest value in the subtree
            rooted at the node, and its parent."""
        parent = None
        node = self
        while node.left() is not None:
            parent = node
            node = node.left()
        return node, parent

    def find_max_in_subtree(self) -> Tuple[Type['TreeNode'], Type['TreeNode']]:
        """Return the node with the largest value in the subtree
            rooted at the node, and its parent."""
        parent = None
        node = self
        while node.right() is not None:
            parent = node
            node = node.right()
        return node, parent
