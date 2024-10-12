from .node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def insert_at_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def delete(self, value):
        if self.head is None:
            return

        current = self.head

        while current:
            if current.data == value:
                if current.prev:  # If not the head node
                    current.prev.next = current.next
                if current.next:  # If not the tail node
                    current.next.prev = current.prev
                if current == self.head:  # If it is the head node
                    self.head = current.next
                if current == self.tail:  # If it is the tail node
                    self.tail = current.prev
                self.count -= 1
                return
            current = current.next


'''
delete(data) - deletes an element with your specified value from the linked list
delete_at_head() - deletes the first element of the list
search(data) - searches for an element with the specified value in the linked list
'''
