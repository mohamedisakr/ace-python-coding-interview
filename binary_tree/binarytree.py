from typing import Any, List, Optional
from node import Node


class BinaryTree:
    def __init__(self, value: Any):
        if value is None:
            raise TypeError("Root value cannot be None")
        self.root = Node(value)

    def pre_order_print(self) -> str:
        result = []
        self._pre_order_helper(self.root, result)
        return ' - '.join(map(str, result)) + ' -'

    def _pre_order_helper(self, node: Node, result: List[Any]) -> None:
        if node:
            result.append(node.value)
            self._pre_order_helper(node.left, result)
            self._pre_order_helper(node.right, result)

    def in_order_print(self) -> str:
        result = []
        self._in_order_helper(self.root, result)
        return ' - '.join(map(str, result)) + ' -'

    def _in_order_helper(self, node: Node, result: List[Any]) -> None:
        if node:
            self._in_order_helper(node.left, result)
            result.append(node.value)
            self._in_order_helper(node.right, result)

    def post_order_print(self) -> str:
        result = []
        self._post_order_helper(self.root, result)
        return ' - '.join(map(str, result)) + ' -'

    def _post_order_helper(self, node: Node, result: List[Any]) -> None:
        if node:
            self._in_order_helper(node.left, result)
            self._in_order_helper(node.right, result)
            result.append(node.value)

    # def pre_order_print(self):
    #     return self._pre_order_print(self.root)

    # def _pre_order_print(self, start):
    #     result = []
    #     self._pre_order_helper(start, result)
    #     return ' - '.join(map(str, result)) + ' -'

    # def _pre_order_helper(self, node, result):
    #     if node:
    #         result.append(node.value)
    #         self._pre_order_helper(node.left, result)
    #         self._pre_order_helper(node.right, result)

    # def in_order_print(self) -> str:
    #     return self._in_order_print(self.root)

    # def _in_order_print(self, start) -> str:
    #     result = []
    #     self._in_order_helper(start, result)
    #     return ' - '.join(map(str, result)) + ' -'

    # def _in_order_helper(self, node, result):
    #     if node:
    #         self._in_order_helper(node.left, result)
    #         result.append(node.value)
    #         self._in_order_helper(node.right, result)
