from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get_head(self) -> Node:
        return self.head

    def is_empty(self) -> bool:
        return self.head is None


'''
insert_at_tail(data) - inserts an element at the end of the linked list
insert_at_head(data) - inserts an element at the start/head of the linked list
delete(data) - deletes an element with your specified value from the linked list
delete_at_head() - deletes the first element of the list
search(data) - searches for an element with the specified value in the linked list
'''
