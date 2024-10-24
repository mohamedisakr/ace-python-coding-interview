from typing import Any
from node import Node


class BinaryTree:
    def __init__(self, value: Any):
        if value is None:
            raise TypeError("Root value cannot be None")
        self.root = Node(value)
