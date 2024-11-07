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

    def search(self, target: Node) -> Node:
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        previous = None
        current = self._head
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError(f'No element with value {
                         target} was found in the list.')
