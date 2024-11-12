from node import Node


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def insert_in_front(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            orig_head = self._head
            self._head = new_node
            self._head.append(orig_head)

    def insert_to_back(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            orig_tail = self._tail
            self._tail = new_node
            self._tail.append(orig_tail)

    def search(self, target) -> Node:  # : Node
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        if self._head is None and self._tail is None:
            return ValueError("Can not delete from empty list!")

        node = self.search(target)

        if node is None:
            return ValueError(f'{target} not found!')  # .data()

        if node.prev() is None:
            self._head = node.next()
            if self._head is None:
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            del node
