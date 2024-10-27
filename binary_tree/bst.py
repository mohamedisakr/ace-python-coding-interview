from node import Node


class BST:
    def __init__(self, value):
        if value is None:
            raise TypeError("Root value cannot be None")
        self.root = Node(value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_helper(self.root, value)

    def insert_helper(self, current, value):
        if current.value < value:
            if current.right:
                self.insert_helper(current.right, value)
            else:
                current.right = Node(value)
        else:
            if current.left:
                self.insert_helper(current.left, value)
            else:
                current.left = Node(value)

    def search(self, value):
        self.search_helper(self.root, value)

    def search_helper(self, current, value):
        if current:
            if current.value == value:
                return True
            elif current.value < value:
                self.search_helper(current.right, value)
            else:
                self.search_helper(current.left, value)
