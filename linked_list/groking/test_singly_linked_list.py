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


# @pytest.mark.skip('postponed till delete function implemented')
def test_insert_to_back_after_deletion():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    # Assume delete method is defined to remove the head element
    sll.delete(10)
    sll.insert_to_back(30)
    assert sll._head.data() == 20
    assert sll._head.next().data() == 30
    assert sll._head.next().next() is None


@pytest.mark.skip('alpha chars')
def test_insert_to_back_with_large_data():
    sll = SinglyLinkedList()
    large_data = "x" * 10000  # Large string data
    sll.insert_to_back(large_data)
    assert sll._head.data == large_data
    assert sll._head.next() is None


# Test cases for insert_to_back function


def test_insert_none_value():
    sll = SinglyLinkedList()
    sll.insert_to_back(None)
    assert sll._head.data() is None
    assert sll._head.next() is None


# @pytest.mark.skip('postponed till clear function implemented')
def test_insert_to_back_after_clear():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.clear()  # Assuming a clear method exists that resets the list

    sll.insert_to_back(30)
    assert sll._head.data() == 30
    assert sll._head.next() is None


def test_insert_to_back_with_mixed_operations():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_in_front(5)  # Assuming insert_in_front method exists
    sll.insert_to_back(25)
    current = sll._head
    assert current.data() == 5
    assert current.next().data() == 10
    assert current.next().next().data() == 20
    assert current.next().next().next().data() == 25
    assert current.next().next().next().next() is None


def test_insert_to_back_with_empty_node():
    sll = SinglyLinkedList()
    empty_node = Node(None)  # Assuming Node can be instantiated with None
    sll.insert_to_back(empty_node)
    assert sll._head.data() == empty_node
    assert sll._head.next() is None


def test_insert_to_back_with_long_chain():
    sll = SinglyLinkedList()
    nodes = [Node(i) for i in range(10)]  # Create a long chain of nodes
    for node in nodes:
        sll.insert_to_back(node.data())
    current = sll._head
    for i in range(10):
        assert current.data() == i
        current = current.next()
    assert current is None


@pytest.mark.skip('positive infinity, negative infinity, NaN (Not a Number)')
def test_insert_to_back_after_edge_insertions():
    sll = SinglyLinkedList()
    sll.insert_to_back(float('inf'))  # Insert positive infinity
    sll.insert_to_back(float('-inf'))  # Insert negative infinity
    sll.insert_to_back(float('nan'))  # Insert NaN (Not a Number)
    assert sll._head.data() == float('inf')
    assert sll._head.next().data() == float('-inf')
    assert sll._head.next().next().data() is float('nan')
    assert sll._head.next().next().next() is None


@pytest.mark.skip('NaN (Not a Number)')
def test_insert_after_exception_handling_nan():
    sll = SinglyLinkedList()
    try:
        sll.insert_to_back(float('nan'))
    except ValueError:
        pass
    sll.insert_to_back(10)
    assert sll._head.data() == nan  # 10
    assert sll._head.next() is None


# Test cases for insert_in_front function


def test_insert_into_empty_list():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    assert sll._head.data() == 10
    assert sll._head.next() is None


def test_insert_single_element_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    assert sll._head.data() == 20
    assert sll._head.next().data() == 10
    assert sll._head.next().next() is None


def test_insert_multiple_elements_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    sll.insert_in_front(30)
    current = sll._head
    assert current.data() == 30
    current = current.next()
    assert current.data() == 20
    current = current.next()
    assert current.data() == 10
    assert current.next() is None


def test_insert_duplicate_elements_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(10)
    current = sll._head
    assert current.data() == 10
    assert current.next().data() == 10
    assert current.next().next() is None


def test_insert_large_number_of_elements_front():
    sll = SinglyLinkedList()
    for i in range(1000):
        sll.insert_in_front(i)
    current = sll._head
    for i in range(999, -1, -1):
        assert current.data() == i
        current = current.next()
    assert current is None


def test_insert_none_value_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(None)
    assert sll._head.data() is None
    assert sll._head.next() is None


def test_insert_various_data_types_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front("string")
    sll.insert_in_front(15.5)
    current = sll._head
    assert current.data() == 15.5
    assert current.next().data() == "string"
    assert current.next().next().data() == 10


def test_insert_to_front_with_large_data():
    sll = SinglyLinkedList()
    large_data = "x" * 10000  # Large string data
    sll.insert_in_front(large_data)
    assert sll._head.data() == large_data
    assert sll._head.next() is None


# @pytest.mark.skip('postponed till clear function implemented')
def test_insert_to_front_after_clear():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    sll.clear()  # Assuming a clear method exists that resets the list
    sll.insert_in_front(30)
    assert sll._head.data() == 30
    assert sll._head.next() is None


@pytest.mark.skip('postponed till delete function implemented')
def test_insert_to_front_after_deletion():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    # Assume delete method is defined to remove the head element
    sll.delete(20)
    sll.insert_in_front(30)
    assert sll._head.data() == 30
    assert sll._head.next().data() == 10
    assert sll._head.next().next() is None


def test_insert_to_front_with_long_chain():
    sll = SinglyLinkedList()

    nodes = [Node(i) for i in range(10)]  # Create a long chain of nodes
    for node in nodes:
        sll.insert_in_front(node.data())

    current = sll._head
    for i in range(9, -1, -1):
        print(f'current: {current.data()}')
        print(f'i: {i}')
        assert current.data() == i
        current = current.next()
    assert current is None


def test_insert_after_exception_handling_front():
    sll = SinglyLinkedList()

    sll.insert_in_front(10)
    assert sll._head.data() == 10
    assert sll._head.next() is None

# Test cases for insert_in_front function


def test_insert_empty_string():
    sll = SinglyLinkedList()
    sll.insert_in_front("")
    assert sll._head.data() == ""
    assert sll._head.next() is None


def test_insert_large_numbers():
    sll = SinglyLinkedList()
    large_number = 10**10
    sll.insert_in_front(large_number)
    assert sll._head.data() == large_number
    assert sll._head.next() is None


def test_insert_nested_data_structures():
    sll = SinglyLinkedList()
    nested_data = {"key": [1, 2, 3], "value": {"inner": "dict"}}
    sll.insert_in_front(nested_data)
    assert sll._head.data() == nested_data
    assert sll._head.next() is None


def test_insert_to_front_in_reverse_order():
    sll = SinglyLinkedList()
    for i in range(10):
        sll.insert_in_front(i)
    current = sll._head
    for i in range(9, -1, -1):
        assert current.data() == i
        current = current.next()
    assert current is None


def test_insert_to_front_with_callable():
    sll = SinglyLinkedList()
    sll.insert_in_front(lambda x: x + 1)
    assert callable(sll._head.data())
    assert sll._head.next() is None


def test_insert_boolean_values():
    sll = SinglyLinkedList()
    sll.insert_in_front(True)
    sll.insert_in_front(False)
    assert sll._head.data() is False
    assert sll._head.next().data() is True
    assert sll._head.next().next() is None


def test_insert_special_characters():
    sll = SinglyLinkedList()
    special_chars = "!@#$%^&*()"
    sll.insert_in_front(special_chars)
    assert sll._head.data() == special_chars
    assert sll._head.next() is None


def test_insert_to_front_and_iterate():
    sll = SinglyLinkedList()
    values = [1, 2, 3, 4]
    for value in values:
        sll.insert_in_front(value)

    current = sll._head
    idx = len(values) - 1
    while current:
        assert current.data() == values[idx]
        current = current.next()
        idx -= 1
    assert current is None


@pytest.mark.skip()
def test_insert_to_front_after_exceptions():
    sll = SinglyLinkedList()
    try:
        sll.insert_in_front(None)
    except TypeError:
        pass
    sll.insert_in_front(10)
    assert sll._head.data() == 10
    assert sll._head.next() is None


@pytest.mark.skip()
def test_insert_after_exception_handling():
    sll = SinglyLinkedList()
    try:
        sll.insert_in_front(None)
    except TypeError:
        pass
    sll.insert_in_front(10)
    assert sll._head.data() == 10
    assert sll._head.next() is None


# Test cases for delete function


def test_delete_from_empty_list():
    sll = SinglyLinkedList()
    with pytest.raises(ValueError, match=r'No element with value .* was found in the list.'):
        sll.delete(10)


def test_delete_single_element_found():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.delete(10)
    assert sll._head is None


def test_delete_single_element_not_found():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    with pytest.raises(ValueError, match=r'No element with value .* was found in the list.'):
        sll.delete(20)


def test_delete_first_element():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    sll.delete(10)
    assert sll._head.data() == 20
    assert sll._head.next().data() == 30
    assert sll._head.next().next() is None


def test_delete_last_element():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    sll.delete(30)
    assert sll._head.data() == 10
    assert sll._head.next().data() == 20
    assert sll._head.next().next() is None


def test_delete_middle_element():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    sll.delete(20)
    assert sll._head.data() == 10
    assert sll._head.next().data() == 30
    assert sll._head.next().next() is None


def test_delete_duplicate_elements():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    sll.delete(20)
    assert sll._head.data() == 10
    assert sll._head.next().data() == 20
    assert sll._head.next().next().data() == 30
    assert sll._head.next().next().next() is None


def test_delete_multiple_elements():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    sll.delete(10)
    sll.delete(30)
    assert sll._head.data() == 20
    assert sll._head.next() is None


def test_delete_none_value():
    sll = SinglyLinkedList()
    sll.insert_to_back(None)
    sll.delete(None)
    assert sll._head is None


def test_delete_various_data_types():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back("string")
    sll.insert_to_back(15.5)
    sll.delete("string")
    assert sll._head.data() == 10
    assert sll._head.next().data() == 15.5


def test_delete_large_data():
    sll = SinglyLinkedList()
    large_data = "x" * 10000  # Large string data
    sll.insert_to_back(large_data)
    sll.delete(large_data)
    assert sll._head is None


def test_delete_first_after_insert_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    sll.delete(20)
    assert sll._head.data() == 10
    assert sll._head.next() is None


def test_delete_last_after_insert_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    sll.delete(10)
    assert sll._head.data() == 20
    assert sll._head.next() is None


def test_delete_middle_after_insert_front():
    sll = SinglyLinkedList()
    sll.insert_in_front(10)
    sll.insert_in_front(20)
    sll.insert_in_front(30)
    sll.delete(20)
    assert sll._head.data() == 30
    assert sll._head.next().data() == 10

# Test cases for delete_from_front function


def test_delete_from_empty_list_from_front():
    sll = SinglyLinkedList()
    result = sll.delete_from_front()
    assert result is None
    assert sll._head is None


def test_delete_single_element():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    result = sll.delete_from_front()
    assert result == 10
    assert sll._head is None


def test_delete_first_of_multiple_elements():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.insert_to_back(30)
    result = sll.delete_from_front()
    assert result == 10
    assert sll._head.data() == 20
    assert sll._head.next().data() == 30
    assert sll._head.next().next() is None


def test_delete_until_empty():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back(20)
    sll.delete_from_front()
    sll.delete_from_front()
    assert sll._head is None


def test_delete_with_none_value():
    sll = SinglyLinkedList()
    sll.insert_to_back(None)
    result = sll.delete_from_front()
    assert result is None
    assert sll._head is None


def test_delete_with_various_data_types():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_to_back("string")
    sll.insert_to_back(15.5)
    result = sll.delete_from_front()
    assert result == 10
    result = sll.delete_from_front()
    assert result == "string"
    result = sll.delete_from_front()
    assert result == 15.5


def test_delete_with_large_number_of_elements():
    sll = SinglyLinkedList()
    for i in range(1000):
        sll.insert_to_back(i)
    result = sll.delete_from_front()
    assert result == 0
    assert sll._head.data() == 1


def test_delete_with_large_data():
    sll = SinglyLinkedList()
    large_data = "x" * 10000  # Large string data
    sll.insert_to_back(large_data)
    result = sll.delete_from_front()
    assert result == large_data
    assert sll._head is None


def test_delete_after_mixed_operations():
    sll = SinglyLinkedList()
    sll.insert_to_back(10)
    sll.insert_in_front(20)
    sll.insert_to_back(30)
    result = sll.delete_from_front()
    assert result == 20
    assert sll._head.data() == 10
