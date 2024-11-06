import pytest
from singly_linked_list import SinglyLinkedList
from node import Node

# Test cases for insert_to_back function


def test_insert_to_empty_list():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    assert sll._head.next() is None
    assert sll._head.data() == 10


def test_insert_single_element():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    assert sll._head.data() == 10
    assert sll._head.next().data() == 20


def test_insert_multiple_elements():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)

    current = sll._head
    assert current.data() == 10
    current = current.next()
    assert current.data() == 20
    current = current.next()
    assert current.data() == 30
    assert current.next() is None


def test_insert_duplicate_elements():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(10)

    current = sll._head
    assert current.data() == 10
    assert current.next().data() == 10
    assert current.next().next() is None


def test_insert_large_number_of_elements():
    sll = SinglyLinkedList()

    for i in range(1000):
        sll.insert_to_back(i)

    current = sll._head
    for i in range(1000):
        assert current.data() == i
        current = current.next()

    assert current is None


def test_insert_various_data_types():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back("string")
    sll.insert_to_back(15.5)

    current = sll._head
    assert current.data() == 10
    assert current.next().data() == "string"
    assert current.next().next().data() == 15.5


@pytest.mark.skip('postponed till delete function implemented')
def test_insert_to_back_after_deletion():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    # Assume delete method is defined to remove the head element
    sll.delete(10)
    sll.insert_to_back(30)
    assert sll._head.data == 20
    assert sll._head.next().data == 30
    assert sll._head.next().next() is None


@pytest.mark.skip('alpha chars')
def test_insert_to_back_with_large_data():
    sll = SinglyLinkedList()
    large_data = "x" * 10000  # Large string data
    sll.insert_to_back(large_data)
    assert sll._head.data == large_data
    assert sll._head.next() is None
