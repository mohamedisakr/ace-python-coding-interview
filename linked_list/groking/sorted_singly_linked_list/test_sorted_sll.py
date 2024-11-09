import pytest
from node import Node
# from sorted_singly_linked_list import SortedSinglyLinkedList
from sorted_sll import SortedSinglyLinkedList

# Test cases for insert function


def test_insert_into_empty_list():
    sll = SortedSinglyLinkedList()
    sll.insert(10)
    assert sll._head.data() == 10
    assert sll._head.next() is None


def test_insert_at_beginning():
    sll = SortedSinglyLinkedList()
    sll.insert(10)
    sll.insert(5)
    assert sll._head.data() == 5
    assert sll._head.next().data() == 10


def test_insert_at_end():
    sll = SortedSinglyLinkedList()
    sll.insert(5)
    sll.insert(10)
    assert sll._head.data() == 5
    assert sll._head.next().data() == 10


def test_insert_in_middle():
    sll = SortedSinglyLinkedList()
    sll.insert(5)
    sll.insert(15)
    sll.insert(10)
    assert sll._head.data() == 5
    assert sll._head.next().data() == 10
    assert sll._head.next().next().data() == 15


def test_insert_duplicates():
    sll = SortedSinglyLinkedList()
    sll.insert(10)
    sll.insert(10)
    sll.insert(10)
    current = sll._head
    assert current.data() == 10
    current = current.next()
    assert current.data() == 10
    current = current.next()
    assert current.data() == 10
    assert current.next() is None


def test_insert_large_number_of_elements():
    sll = SortedSinglyLinkedList()
    elements = list(range(1000, 0, -1))  # Insert 1000 to 1
    for elem in elements:
        sll.insert(elem)
    current = sll._head
    for i in range(1, 1001):
        assert current.data() == i
        current = current.next()


def test_insert_none_value():
    sll = SortedSinglyLinkedList()
    sll.insert(None)
    assert sll._head.data() is None
    assert sll._head.next() is None


@pytest.mark.skip('mixed data types')
def test_insert_mixed_data_types():
    sll = SortedSinglyLinkedList()
    sll.insert(10)
    sll.insert("string")
    sll.insert(5.5)
    sll.insert("another string")
    sll.insert(2)
    # The list will maintain insertion order since it's sorted,
    # this is for hypothetical purposes to show mixed data() handling.
    current = sll._head
    assert current.data() == 10
    assert current.next().data() == "string"
    assert current.next().next().data() == 5.5
    assert current.next().next().next().data() == "another string"
    assert current.next().next().next().next().data() == 2


def test_insert_with_large_values():
    sll = SortedSinglyLinkedList()
    large_number = 10**18
    sll.insert(large_number)
    sll.insert(large_number - 1)
    assert sll._head.data() == large_number - 1
    assert sll._head.next().data() == large_number
