from typing import Optional
from node import Node


class BinarySearchTree:
    # def __init__(self):
    def __init__(self, value) -> None:
        # self._root = None
        if value is None:
            raise TypeError("Root value cannot be None")
        self._root = Node(value)

    def _search(self, value: any) -> tuple[Optional[type[Node]], type[Node]]:
        """Returns a tuple.
           The first element in the tuple is the node containing the target value,
           or None if not found. If the tree contains duplicates, it returns the first 
           node traversed that contains the target value.
           The second element in the tuple is the parent of the node in the first position.
           If the target wasn't found or if it was the root, the parent is set to None.
        """
        parent = None
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None

    # def _search(self, value):
    #     parent = None
    #     node = self._root
    #     if node is not None:
    #         if node._value == value:
    #             return node, parent
    #         elif node._value > value:
    #             parent = node
    #             node = node.get_left()
    #         else:
    #             parent = node
    #             node = node.get_right()
    #     return None, None
