from node import Node


class DLLSentinel:

    def __init__(self, get_key_func=None):
        """Initialize the sentinel of a circular doubly linked list with a sentinel.

        Arguments:
        get_key_func -- an optional function that returns the key for the
        objects stored. May be a static function in the object class. If 
        omitted, then identity function is used.
        """
        self.sentinel = Node(None)  # holds None as data

        # the sentinel points to itself in an empty list
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        if get_key_func is None:
            self.get_key = lambda x: x   # return self
        else:
            self.get_key = get_key_func  # return key defined by user

    def search(self, k):
        """Search a circular doubly linked list with a sentinel for a node with key k.

        Returns:
        current -- node with key k or None if not found
        """
        current = self.sentinel.next
        # Go down the list until key k is found.
        # Need to test for the sentinel to avoid calling get_key(None) when current is the sentinel.
        while current is not self.sentinel and self.get_key(current.data) != k:
            current = current.next

        if current is self.sentinel:  # went through the whole list?
            return None         # yes, so no node had key
        else:
            return current            # found it!

    def insert(self, data, after_node):
        """Insert a node with data after node after_node.  Return the new node."""
        # construct a node new_node
        new_node = Node(data)
        # new_node's successor is after_node's successor
        new_node.next = after_node.next
        # new_node's predecessor is after_node
        new_node.prev = after_node
        # new_node comes before after_node's successor
        after_node.next.prev = new_node
        # new_node is now after_node's successor
        after_node.next = new_node
        return new_node

    def prepend(self, data):
        """Insert a node with data as the head of a circular doubly linked list with a sentinel.
        Return the new node."""
        return self.insert(data, self.sentinel)

    def append(self, data):
        """Append a node with data to the tail of a circular doubly linked list with a sentinel.
        Return the new node."""
        return self.insert(data, self.sentinel.prev)

    def delete(self, node_to_delete):
        """Remove a node node_to_delete from the a circular doubly linked list with a sentinel.

        Assumption:
        node_to_delete is a node in the linked list. 
        """
        if node_to_delete is self.sentinel:
            raise RuntimeError("Cannot delete sentinel.")
        node_to_delete.prev.next = node_to_delete.next  # point prev to next
        node_to_delete.next.prev = node_to_delete.prev  # point next to prev

    def delete_all(self):
        """Delete all nodes in a circular doubly linked list with a sentinel."""
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def iterator(self):
        """Iterator from the head of a circular doubly linked list with a sentinel."""
        current = self.sentinel.next
        while current is not self.sentinel:
            yield current.get_data()
            current = current.next

    def __iter__(self):
        self.current = self.sentinel.next
        return self

    def __next__(self):
        if self.current == self.sentinel:
            raise StopIteration
        data = self.current.get_data()
        self.current = self.current.next
        return data

    def copy(self):
        """Return a copy of this circular doubly linked list with a sentinel."""
        c = DLLSentinel(self.get_key)      # c is the copy
        x = self.sentinel.next
        while x != self.sentinel:
            c.append(x.data)   # append a node with x's data to c
            x = x.next
        return c

    def __str__(self):
        """Return this circular doubly linked list with a sentinel formatted as a list."""
        x = self.sentinel.next
        string = "["
        while x != self.sentinel:
            string += (str(x) + ", ")
            x = x.next
        string += (str(x) + "]")
        return string


# # Testing
# if __name__ == "__main__":

#     from key_object import KeyObject

#     # Insert.
#     linked_list1 = DLLSentinel()
#     for i in range(10):
#         linked_list1.prepend(i)
#     print(linked_list1)

#     # Search.
#     print(linked_list1.search(5))

#     # Copy.
#     linked_list2 = linked_list1.copy()
#     linked_list2.append(99)
#     print(linked_list1)
#     print(linked_list2)

#     # Delete.
#     linked_list2 = DLLSentinel()
#     linked_list2.prepend(5)
#     linked_list2.prepend(6)
#     linked_list2.prepend(7)
#     print(linked_list2)
#     x = linked_list2.search(6)  # should be 6
#     print(x)
#     linked_list2.delete(x)
#     print(linked_list2.search(6))  # unsuccessful search
#     print(linked_list2)

#     # Delete sentinel error.
#     try:
#         linked_list2.delete(linked_list2.sentinel)
#     except RuntimeError as e:
#         print(e)

#     # Object.
#     linked_list3 = DLLSentinel(KeyObject.get_key)
#     list1 = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "HI", "NH", "NY"]
#     for i in range(len(list1)):
#         linked_list3.append(KeyObject(list1[i], i))
#     print(linked_list3)
#     node5 = linked_list3.search(5)  # CO has key 5
#     print(node5)
#     linked_list3.insert(KeyObject("VT", 17), node5)  # insert VT after CO
#     linked_list3.delete(node5)                       # delete CO
#     print(linked_list3)
