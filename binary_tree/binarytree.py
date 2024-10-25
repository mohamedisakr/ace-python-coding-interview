from typing import Any, List, Optional
from node import Node
from my_queue import MyQueue


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

    # def level_order_print(self, start: Node):
    #     if start is None:
    #         return

    #     que = MyQueue()
    #     que.enqueue(start)
    #     traverse = ""

    #     while len(que) > 0:
    #         traverse += f'{que.peek()} -'
    #         node = que.dequeue()

    #         if node.left:
    #             que.enqueue(node.left)

    #         if node.right:
    #             que.enqueue(node.right)

    #     return traverse


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(tree.level_order_print(tree.root))
