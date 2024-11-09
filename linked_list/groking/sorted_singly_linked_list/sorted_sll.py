from typing import Any, Optional
from node import Node


class SortedSinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert(self, value: Any):
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
