from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, data):
        new_node = Node(data)

        if self.is_empty() is True:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.is_empty() is True:
            self.head = new_node
        else:
            first = self.head
            while first is not None:  # .next
                first = first.next

            print(f'tail value {first.data}')
            first.next = new_node
            # new_node.next = None

    def print_list(self):
        if self.is_empty() is True:
            print('linked list is empty')
            return False
        else:
            first = self.head
            while first.next is not None:
                print(first.data, end=' -> ')
                first = first.next
        return True


# test
linkList = LinkedList()
# print(linkList.is_empty())
# linkList.print_list()

for i in range(4, 0, -1):
    linkList.insert_at_head(i)

linkList.insert_at_tail(5)
linkList.print_list()
