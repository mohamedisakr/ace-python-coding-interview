from typing import Optional, Any
from node import Node
from stack import Stack


class BinarySearchTree:
    """A class modeling the binary search tree data structure."""

    def __init__(self) -> None:
        # if value is None:
        #     raise TypeError("Root value cannot be None")
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

    def insert(self, value: Any) -> None:
        """Insert a new value into the tree.

        Args:
            value: The new element to be added to the tree.
        """
        node = self._root
        if node is None:
            # Empty tree
            self._root = Node(value)
        else:
            while node is not None:  # while True:  # node can never be None here
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

    def delete(self, value: any) -> None:
        """ Delete a value from the tree.
            If the value is not found, raise a ValueError.
            If the tree is empty, raise a ValueError.
            If the tree contains duplicates, delete the first node found.
        Args:
            value: The element to be deleted from the tree.
        """
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')

        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            # The node has at most only one child
            if parent is None:
                # The node is the root
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else:  # The node N has two children.
            # Find and remove the node M with the largest value in the left subtree of N.
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None:  # M is the left child of N.
                new_node = Node(max_node.value(), None, node.right())
            else:
                new_node = Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            # Then  replace the node to be deleted with a new node with M.value(),
            # and the same subtrees as N.
            if parent is None:
                # The node is the root
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)

    def __iter__(self):
        """
        Iterate over the values in the BST.

        Parameters:
            None

        Functionality:
            Iterates over the values in the BST. The iteration starts at the root of the BST and
            traverses the tree using inorder traversal.
        """
        current = self._root
        stack = Stack()
        while current is not None or len(stack) > 0:
            if current is None:
                current = stack.pop()
                yield current.value()
                current = current.right()
            else:
                while current.left() is not None:
                    stack.push(current)
                    current = current.left()
                yield current.value()
                current = current.right()
