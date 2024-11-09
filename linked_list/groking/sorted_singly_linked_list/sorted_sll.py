from typing import Any, Optional
from node import Node


class SortedSinglyLinkedList:
    """ A sorted version of the singly-linked lists.
    """

    def __init__(self):
        self._head = None

    def insert(self, value: Any) -> None:
        """
        Insert a new value into the sorted singly linked list.

        Parameters:
            new_data (Any): The new data value to insert.

        Returns:
            None                
        """
        previous = None
        current = self._head

        while current is not None:
            if current.data() >= value:
                if previous is None:
                    self._head = Node(value, current)
                else:
                    previous.append(Node(value, current))
                return
            previous = current
            current = current.next()

        if previous is None:
            self._head = Node(value)
        else:
            previous.append(Node(value, None))

    def insert_in_front(self, value: Any) -> None:
        raise NotImplementedError(
            'This method is not available for sorted lists')

    def insert_to_back(self, value: Any) -> None:
        raise NotImplementedError(
            'This method is not available for sorted lists')
