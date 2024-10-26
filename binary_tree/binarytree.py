from typing import Any, List, Optional
from node import Node
from my_queue import MyQueue
from my_stack import MyStack


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

    def level_order_print(self) -> str:
        return self._level_order_print(self.root)

    def _level_order_print(self, start: Node) -> str:
        if start is None:
            return ""

        que = MyQueue()
        que.enqueue(start)
        traverse = ""

        while len(que) > 0:
            node = que.dequeue()
            traverse += f'{node.value} - '

            if node.left:
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)

        return traverse.strip(" - ") + " -"

    def reverse_level_order_print(
        self): return self._reverse_level_order_print(self.root)

    def _reverse_level_order_print(self, start: Node) -> str:
        if start is None:
            return ""

        queue = MyQueue()
        stack = MyStack()

        queue.enqueue(start)
        traverse = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traverse += f'{node.value}-'
        return traverse

    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size_(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)
