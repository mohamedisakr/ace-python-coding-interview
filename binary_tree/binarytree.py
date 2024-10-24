from typing import Any
from node import Node


class BinaryTree:
    def __init__(self, value: Any):
        if value is None:
            raise TypeError("Root value cannot be None")
        self.root = Node(value)

    def pre_order_print(self, start):
        traverse = ''
        if start:
            traverse += (f'{str(start.value)} -')
            traverse += self.pre_order_print(start.left)
            traverse += self.pre_order_print(start.right)
        return traverse
