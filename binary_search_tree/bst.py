from typing import Optional, Any
from node import Node


class BinarySearchTree:
    """A class modeling the binary search tree data structure."""

    def __init__(self) -> None:
        self._root = None

    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'

    def __str__(self) -> str:
        return Node._node_str(self._root)

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

    def contains(self, value: any) -> bool:
        """Return True if the tree contains the value, False otherwise.

        Args:
            value: The element to be searched in the tree.
        Returns: True if the value is found in the tree, False otherwise.
        """
        return self._search(value)[0] is not None

    def insert(self, value: any) -> None:
        """Insert a new value into the tree.

        Args:
            value: The new element to be added to the tree.
        """
        node = self._root
        if node is None:
            # Empty tree
            self._root = Node(value)
        else:
            while True:  # node can never be None here
                if value <= node.value():
                    if node.left() is None:
                        # We have found the right spot for value
                        node.set_left(Node(value))
                        break
                    else:
                        # We keep traversing the left branch
                        node = node.left()
                elif node.right() is None:
                    # We have found the right spot for value
                    node.set_right(Node(value))
                    break
                else:
                    # We keep traversing the right branch
                    node = node.right()


# class BinarySearchTree:
#     def __init__(self, value) -> None:
#         if value is None:
#             raise TypeError("Root value cannot be None")
#         self._root = Node(value)

#     def _search(self, value: any) -> tuple[Optional[type[Node]], type[Node]]:
#         """Returns a tuple.
#            The first element in the tuple is the node containing the target value,
#            or None if not found. If the tree contains duplicates, it returns the first
#            node traversed that contains the target value.
#            The second element in the tuple is the parent of the node in the first position.
#            If the target wasn't found or if it was the root, the parent is set to None.
#         """
#         parent = None
#         node = self._root
#         while node is not None:
#             node_val = node.value
#             if node_val == value:
#                 return node, parent
#             elif value < node_val:
#                 parent = node
#                 node = node.left  # .left()
#             else:
#                 parent = node
#                 node = node.right
#         return None, None

#     def insert(self, value: Any) -> None:
#         """Insert a new value into the tree.

#         Args:
#             value: The new element to be added to the tree.
#         """
#         node = self._root
#         if node is None:
#             # Empty tree
#             self._root = Node(value)
#         else:
#             while node is not None:  # True: # node can never be None here
#                 if value <= node.value:
#                     if node.left is None:
#                         # We have found the right spot for value
#                         node.set_left(Node(value))
#                         break
#                     else:
#                         # We keep traversing the left branch
#                         node = node.left
#                 elif node.right is None:
#                     # We have found the right spot for value
#                     node.set_right(Node(value))
#                     break
#                 else:
#                     # We keep traversing the right branch
#                     node = node.right
