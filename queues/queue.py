from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.items


queue_obj = MyQueue()
