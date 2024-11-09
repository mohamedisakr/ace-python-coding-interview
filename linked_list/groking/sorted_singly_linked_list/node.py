from typing import Any, Optional


class Node:
    """
        A node in a singly linked list. Each node contains data and
        a reference to the next node.

        Attributes:

            data: The data held in the node. Can be any arbitrary object.
            _next: A reference to the next node in the list.
    """

    def __init__(self, data: Any, next_node: Optional['Node'] = None) -> None:
        """
            Initialize a new Node object.

            Parameters:

            - data (Any): The data for the node. Can be any arbitrary object.
            - next_node (Node, optional): The next Node in the list. Defaults to None.
        """
        self._data = data
        self._next = next_node

    def data(self) -> Any:
        """
            Get the data stored in this node.

            Parameters:
                None

            Returns:
                Any: The data stored in this node. Can be any arbitrary object.
        """
        return self._data

    def next(self) -> 'Node':
        """
            Return the successor of the current node.

            Parameters:
                None

            Returns:
                Node: The next node in the singly-linked list.
        """
        return self._next

    def has_next(self) -> bool:
        """
            Check if the node has a successor.

            Parameters:
                None

            Returns:
                bool: True if the node has a next node, False otherwise.
        """
        return self._next is not None

    def append(self, node: Optional['Node']) -> None:
        self._next = node

    def __str__(self) -> str:
        """
        Return a string representation of the node's data.

        Parameters:
            None

        Returns:
            str: String representation of the node's data.
        """
        return str(self.data())

    def __repr__(self) -> str:
        """
        Return a string (internal) representation of the node's data.

        Parameters:
            None

        Returns:
            str: String representation of the node's data.
        """
        return repr(self.data())
