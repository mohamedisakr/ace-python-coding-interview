from .node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_at_tail(self, data):
        # Insert a new node with given data at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        last = self.head
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        self.count += 1
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
                self.count -= 1
                return True
            previous = current
            current = current.next
        return False

    def length(self):
        return self.count

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

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
        if self.head is None:
            return None

        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def remove_duplicates(self):
        visited_map = {}
        current = self.head
        previous = None

        while current:
            if current.data in visited_map:
                previous.next = current.next
            else:
                visited_map[current.data] = True
                previous = current
            current = current.next

    def intersection(self, other):
        intersec = set()
        result = []

        current = self.head
        while current:
            intersec.add(current.data)
            current = current.next

        current = other.head
        seen = set()
        while current:
            if current.data in intersec and current.data not in seen:
                result.append(current.data)
                seen.add(current.data)
            current = current.next

        return result

    def union(self, other):
        union_set = set()

        current = self.head
        while current:
            union_set.add(current.data)
            current = current.next

        current = other.head
        while current:
            union_set.add(current.data)
            current = current.next

        return union_set

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
