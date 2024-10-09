from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        # if self.head is None:
        #     return True
        # return False
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        # Insert a new node with given data at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('NULL')


# test
linkList = LinkedList()
# print(linkList.is_empty())
# linkList.print_list()

for i in range(4, 0, -1):
    linkList.insert_at_head(i)

linkList.insert_at_tail(5)
linkList.print_list()

value = 2
print(f'search for {value} is {
      'found' if linkList.search(value) else 'not found'}')


value = 10
print(f'search for {value} is {
      'found' if linkList.search(value) else 'not found'}')

# delete value
value_to_delete = 4
