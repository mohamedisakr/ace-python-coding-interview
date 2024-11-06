from node import Node


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def insert_to_back(self, data):
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))
