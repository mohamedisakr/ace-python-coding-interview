from node import Node


class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        self.insert_helper(self.root, value)

    def insert_helper(self, current, value):
        if current.data < value:
            if current.right:
                self.insert_helper(current.right, value)
            else:
                current.right = Node(value)
        else:
            if current.left:
                self.insert_helper(current.left, value)
            else:
                current.left = Node(value)
