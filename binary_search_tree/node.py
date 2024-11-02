from typing import Optional, Tuple, Any


class Node:
    """A class modeling the nodes of the binary search tree."""

    @staticmethod
    def _node_str(node: Optional['Node']) -> str:
        return str(node) if node is not None else ''

    def __init__(self,
                 value: Any,
                 left: Optional['Node'] = None,
                 right: Optional['Node'] = None) -> None:
        self._value = value
        self._left = left
        self._right = right

    def __str__(self) -> str:
        left_str = Node._node_str(self._left)
        right_str = Node._node_str(self._right)
        return f'{self._value} ({left_str})({right_str})'

    @property
    def value(self) -> Any:
        """Return the value of the node."""
        return self._value

    @property
    def left(self) -> Optional['Node']:
        """Return a reference to the left child of the node."""
        return self._left

    @property
    def right(self) -> Optional['Node']:
        """Return a reference to the right child of the node."""
        return self._right

    @left.setter
    def set_left(self, node: Optional['Node']) -> None:
        """Set the left child of the node. The old value will be lost."""
        self._left = node

    @right.setter
    def set_right(self, node: Optional['Node']) -> None:
        """Set the right child of the node. The old value will be lost."""
        self._right = node

    def find_min_in_subtree(self) -> Tuple[Optional['Node'], Optional['Node']]:
        """Return the node with the smallest value in the subtree rooted at the node, 
        and its parent."""
        parent = None
        node = self
        while node.left is not None:
            parent = node
            node = node.left
        return node, parent

    def find_max_in_subtree(self) -> Tuple[Optional['Node'], Optional['Node']]:
        """Return the node with the largest value in the subtree rooted at the node, 
        and its parent."""
        parent = None
        node = self
        while node.right is not None:
            parent = node
            node = node.right
        return node, parent
