from node import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert_to_back(self, data) -> None:
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))

    def insert_in_front(self, data) -> None:
        old_head = self._head
        self._head = Node(data, old_head)
