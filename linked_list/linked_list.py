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
        temp = self.head
        if temp is None:
            return False

        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def print_list(self):
        temp = self.head  # Start from the head of the list
        while temp:
            print(temp.data, end=' -> ')  # Print the data in the current node
            temp = temp.next  # Move to the next node
        print('NULL')  # Ensures the output is followed by a new line


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
