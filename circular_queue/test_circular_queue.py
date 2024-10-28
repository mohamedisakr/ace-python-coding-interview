import pytest
from circular_queue_dll import MyCircularQueue

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

# --- other test cases -----


# @pytest.fixture
# def circular_queue():
#     return MyCircularQueue(3)


def test_enqueue_empty_queue(circular_queue):
    assert circular_queue.enQueue(5) == True
    assert circular_queue.Front() == 5
    assert circular_queue.Rear() == 5


def test_enqueue_partially_filled_queue(circular_queue):
    circular_queue.enQueue(5)
    assert circular_queue.enQueue(10) == True
    assert circular_queue.Front() == 5
    assert circular_queue.Rear() == 10


def test_enqueue_full_queue(circular_queue):
    circular_queue.enQueue(5)
    circular_queue.enQueue(10)
    circular_queue.enQueue(15)
    assert circular_queue.enQueue(20) == False


def test_dequeue_non_empty_queue(circular_queue):
    circular_queue.enQueue(5)
    assert circular_queue.deQueue() == True
    assert circular_queue.isEmpty() == True


def test_dequeue_empty_queue(circular_queue):
    assert circular_queue.deQueue() == False


def test_front_non_empty_queue(circular_queue):
    circular_queue.enQueue(5)
    assert circular_queue.Front() == 5


def test_front_empty_queue(circular_queue):
    assert circular_queue.Front() == -1


def test_rear_non_empty_queue(circular_queue):
    circular_queue.enQueue(5)
    assert circular_queue.Rear() == 5


# def test_rear_empty_queue(circular_queue):
#     assert circular
