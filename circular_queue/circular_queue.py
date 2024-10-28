from typing import Optional
from node import Node


class MyCircularQueue:
    def __init__(self, k: int):
        self.space: int = k
        self.left = Node(0)
        self.right = Node(0, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value, self.right.previous, self.right)
        self.right.previous.next = new_node
        self.right.previous = new_node
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.previous = self.left
        self.space += 1
        return True

    def front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.value

    def rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.previous.value

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

    def __repr__(self) -> str:
        values = []
        current = self.left.next
        while current != self.right:
            values.append(current.value)
            current = current.next
        return f"MyCircularQueue({values})"
