from typing import Optional


class TreeNode:
    # left: int, right: int
    def __init__(self, key: int, index: Optional[int] = None) -> None:
        self._key: int = key
        self._index: Optional[int] = index
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None


class BinaryTree:
    def __init__(self) -> None:
        self._root = None
