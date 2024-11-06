import pytest
from dynamic_sorted import DynamicSortedArray
# Test cases for insert function


def test_insert_into_empty_array():
    dsa = DynamicSortedArray(1)
    dsa.insert(10)
    assert dsa._array[0] == 10
    assert dsa._size == 1


def test_insert_single_value():
    dsa = DynamicSortedArray(2)
    dsa.insert(10)
    assert dsa._array[0] == 10
    assert dsa._size == 1


def test_insert_multiple_values():
    dsa = DynamicSortedArray(2)
    dsa.insert(10)
    dsa.insert(20)
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert dsa._size == 2


def test_insert_and_resize():
    dsa = DynamicSortedArray(2)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)  # Should trigger resize
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert dsa._array[2] == 30
    assert dsa._size == 3
    assert dsa._capacity == 4  # Assuming resize doubles the capacity


def test_insert_duplicate_values():
    dsa = DynamicSortedArray(2)
    dsa.insert(10)
    dsa.insert(10)  # Inserting a duplicate value
    assert dsa._array[0] == 10
    assert dsa._array[1] == 10
    assert dsa._size == 2


def test_insert_larger_than_initial_capacity():
    dsa = DynamicSortedArray(2)
    for i in range(5):  # Inserting more than initial capacity
        dsa.insert(i * 10)
    assert dsa._size == 5
    assert dsa._capacity >= 5  # Check capacity has resized


@pytest.mark.skip('alpha charaters')
def test_insert_non_integer_values():
    dsa = DynamicSortedArray(2, 'u')
    dsa.insert(ord('a'))
    dsa.insert(ord('b'))
    assert dsa._array[0] == ord('a')
    assert dsa._array[1] == ord('b')
    assert dsa._size == 2


def test_insert_at_full_capacity():
    dsa = DynamicSortedArray(3)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    dsa.insert(40)  # Should trigger resize
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert dsa._array[2] == 30
    assert dsa._array[3] == 40
    assert dsa._size == 4
    assert dsa._capacity == 6  # Depending on resize factor


def test_insert_after_multiple_resizes():
    dsa = DynamicSortedArray(2)
    for i in range(10):  # Multiple insertions to trigger multiple resizes
        dsa.insert(i * 10)
    for i in range(10):
        assert dsa._array[i] == i * 10
    assert dsa._size == 10
    assert dsa._capacity >= 10  # Ensure capacity is enough to hold all elements


# Other test cases for insert function


def test_insert_negative_values():
    dsa = DynamicSortedArray(5)
    dsa.insert(-10)
    dsa.insert(-20)
    dsa.insert(0)
    assert dsa._array[0] == -20
    assert dsa._array[1] == -10
    assert dsa._array[2] == 0
    assert dsa._size == 3


def test_insert_values_in_reverse_order():
    dsa = DynamicSortedArray(5)
    dsa.insert(30)
    dsa.insert(20)
    dsa.insert(10)
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert dsa._array[2] == 30
    assert dsa._size == 3


def test_insert_values_with_large_gaps():
    dsa = DynamicSortedArray(5)
    dsa.insert(1000)
    dsa.insert(-1000)
    dsa.insert(500)
    assert dsa._array[0] == -1000
    assert dsa._array[1] == 500
    assert dsa._array[2] == 1000
    assert dsa._size == 3


def test_insert_at_array_boundaries():
    dsa = DynamicSortedArray(2)
    dsa.insert(1)
    dsa.insert(2)
    dsa.insert(3)  # Should trigger resize
    assert dsa._array[0] == 1
    assert dsa._array[1] == 2
    assert dsa._array[2] == 3
    assert dsa._size == 3
    assert dsa._capacity == 4  # Assuming resize doubles the capacity


def test_insert_same_values_multiple_times():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(10)
    dsa.insert(10)
    assert dsa._array[0] == 10
    assert dsa._array[1] == 10
    assert dsa._array[2] == 10
    assert dsa._size == 3


def test_insert_float_values():
    dsa = DynamicSortedArray(5, 'd')
    dsa.insert(10.5)
    dsa.insert(20.1)
    dsa.insert(15.3)
    assert dsa._array[0] == 10.5
    assert dsa._array[1] == 15.3
    assert dsa._array[2] == 20.1
    assert dsa._size == 3

# Test cases for delete function


def test_delete_from_empty_array():
    dsa = DynamicSortedArray(1)
    with pytest.raises(ValueError, match="Unable to delete element 10: the entry is not in the array"):
        dsa.delete(10)


def test_delete_existing_value():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    dsa.delete(20)
    assert dsa._size == 2
    assert dsa._array[0] == 10
    assert dsa._array[1] == 30
    assert 20 not in dsa._array[:dsa._size]


def test_delete_non_existing_value():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    with pytest.raises(ValueError, match="Unable to delete element 40: the entry is not in the array"):
        dsa.delete(40)


def test_delete_first_element():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    dsa.delete(10)
    assert dsa._size == 2
    assert dsa._array[0] == 20
    assert dsa._array[1] == 30
    assert 10 not in dsa._array[:dsa._size]


def test_delete_last_element():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    dsa.delete(30)
    assert dsa._size == 2
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert 30 not in dsa._array[:dsa._size]


def test_delete_after_multiple_insertions():
    dsa = DynamicSortedArray(2)
    for i in range(10):  # Multiple insertions to trigger multiple resizes
        dsa.insert(i)
    dsa.delete(0)
    dsa.delete(9)
    assert dsa._size == 8
    for i in range(8):
        assert dsa._array[i] == i + 1
    assert 0 not in dsa._array[:dsa._size]
    assert 9 not in dsa._array[:dsa._size]


def test_delete_duplicate_values():
    dsa = DynamicSortedArray(5)
    dsa.insert(10)
    dsa.insert(10)
    dsa.insert(20)
    dsa.delete(10)
    assert dsa._size == 2
    assert dsa._array[0] == 10
    assert dsa._array[1] == 20
    assert dsa._array[2] != 10


def test_delete_negative_values():
    dsa = DynamicSortedArray(5)
    dsa.insert(-10)
    dsa.insert(-20)
    dsa.insert(0)
    dsa.delete(-10)
    assert dsa._size == 2
    assert dsa._array[0] == -20
    assert dsa._array[1] == 0
    assert -10 not in dsa._array[:dsa._size]


def test_delete_triggers_resize():
    dsa = DynamicSortedArray(4)
    dsa.insert(10)
    dsa.insert(20)
    dsa.insert(30)
    dsa.insert(40)
    dsa.delete(10)
    dsa.delete(20)
    assert dsa._size == 2
    assert dsa._capacity == 4  # Assuming the capacity halves when size <= capacity // 4
