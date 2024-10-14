from doubly_linked_list.doubly_linked_list import DoublyLinkedList


class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length() == 0

    def front(self):
        return self.items.get_head() if not self.is_empty() else None

    def rear(self):
        return self.items.get_tail() if not self.is_empty() else None

    def size(self):
        return self.items.length()

    def enqueue(self, value):
        self.items.insert_at_tail(value)

    def dequeue(self):
        self.items.delete_at_head()

    def reverseK(self, k):
        # self.items.rev
        pass

    def print_list(self):
        # print(self.items)
        return str(self.items)


queue_obj = MyQueue()
