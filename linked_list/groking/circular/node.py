class Node:

    def __init__(self, data):
        """Initialize a node of a circular doubly linked list with a sentinel with the given data."""
        self.prev = None
        self.next = None
        self.data = data

    def get_data(self):
        """Return data."""
        return self.data

    def __str__(self):
        """Return data as a string."""
        return str(self.data)
