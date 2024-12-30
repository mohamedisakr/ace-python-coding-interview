from typing import Dict, Optional


class TreeNode:
    def __init__(self, key: int, index: Optional[int] = None) -> None:
        self._key: int = key
        self._index: Optional[int] = index
        self._left: Optional[TreeNode] = None
        self._right: Optional[TreeNode] = None


class BinaryTree:
    def __init__(self) -> None:
        self._root: Optional[TreeNode] = None
        self._nodes: Dict[int, TreeNode] = None

    def inorder(self) -> None:
        def _inorder(node: Optional[TreeNode]) -> None:
            if node:
                self._inorder(node.left)
                print(f"({node._index}) {node._key}")
                self._inorder(node._right)

        if self._root:
            _inorder(self._root)
