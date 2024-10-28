import pytest
from typing import Optional


class Node:
    def __init__(self, value: int, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.value: int = value
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next


class MyCircularQueue:
    def __init__(self, k: int):
        self.size: int = k
        self.count: int = 0
        self.head: Node = Node(0)
        self.tail: Node = Node(0, self.head)
        self.head.next = self.tail

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node: Node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.value

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

    def __repr__(self) -> str:
        values = []
        current = self.head.next
        while current != self.tail:
            values.append(current.value)
            current = current.next
        return f"MyCircularQueue({values})"

# Fixtures


@pytest.fixture
def circular_queue():
    return MyCircularQueue(3)

# Test Cases


def test_init(circular_queue):
    assert circular_queue.size == 3
    assert circular_queue.count == 0
    assert circular_queue.isEmpty()
    assert not circular_queue.isFull()


def test_enqueue(circular_queue):
    assert circular_queue.enQueue(1) == True
    assert circular_queue.enQueue(2) == True
    assert circular_queue.enQueue(3) == True
    assert circular_queue.enQueue(4) == False  # Queue should be full now
    assert circular_queue.isFull()


def test_dequeue(circular_queue):
    circular_queue.enQueue(1)
    circular_queue.enQueue(2)
    assert circular_queue.deQueue() == True
    assert circular_queue.deQueue() == True
    assert circular_queue.deQueue() == False  # Queue should be empty now
    assert circular_queue.isEmpty()


def test_front(circular_queue):
    assert circular_queue.Front() == -1  # Empty queue
    circular_queue.enQueue(1)
    assert circular_queue.Front() == 1
    circular_queue.enQueue(2)
    assert circular_queue.Front() == 1


def test_rear(circular_queue):
    assert circular_queue.Rear() == -1  # Empty queue
    circular_queue.enQueue(1)
    assert circular_queue.Rear() == 1
    circular_queue.enQueue(2)
    assert circular_queue.Rear() == 2


def test_isEmpty(circular_queue):
    assert circular_queue.isEmpty() == True
    circular_queue.enQueue(1)
    assert circular_queue.isEmpty() == False


def test_isFull(circular_queue):
    assert circular_queue.isFull() == False
    circular_queue.enQueue(1)
    circular_queue.enQueue(2)
    circular_queue.enQueue(3)
    assert circular_queue.isFull() == True


def test_enqueue_dequeue_sequence(circular_queue):
    assert circular_queue.enQueue(1) == True
    assert circular_queue.enQueue(2) == True
    assert circular_queue.deQueue() == True
    assert circular_queue.enQueue(3) == True
    assert circular_queue.enQueue(4) == True
    assert circular_queue.isFull() == True
    assert circular_queue.Front() == 2
    assert circular_queue.Rear() == 4

# To run the tests, use the command:
# pytest your_test_file.py
