from typing import Optional, Tuple


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def left(self):
        return self.left

    def right(self):
        return self.right

    def value(self):
        return self._value

    def set_left(self, node):  # : Optional[TreeNode]
        self._left = node

    def set_right(self, node):
        self._right = node


class BinarySearchTree:
    def __init__(self):
        self._root: TreeNode = None

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

    def find_max(self) -> Optional[Tuple[TreeNode, TreeNode]]:
        parent = None
        current = self._root

        while current.right():
            parent = current
            current = current.right()

        return current, parent

    def find_min(self) -> Optional[Tuple[TreeNode, TreeNode]]:
        parent = None
        current = self._root

        while current.left():
            parent = current
            current = current.left()

        return current, parent
