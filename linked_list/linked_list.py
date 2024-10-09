from .node import Node


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

    def length(self):
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous

    def detect_loop(self) -> bool:
        # Floyd's cycle-finding (tortoise and hare) algorithm
        # Initialize two pointers, slow and fast
        slow, fast = self.head, self.head

        # Traverse the list with two pointers
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by one step
            fast = fast.next.next     # Move fast pointer by two steps

            # Check if the two pointers meet
            if slow == fast:
                return True

        # If no loop is found
        return False

    def find_mid(self) -> int:
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('NULL')


'''
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
'''
