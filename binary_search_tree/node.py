class Node:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node
