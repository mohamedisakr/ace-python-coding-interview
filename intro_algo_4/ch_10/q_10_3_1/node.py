from typing import Dict, Optional, List, Tuple


class TreeNode:
    def __init__(self, key: int, index: Optional[int] = None) -> None:
        self._key: int = key
        self._index: Optional[int] = index
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def index(self):
        return self._index

    @property
    def key(self):
        return self._key
