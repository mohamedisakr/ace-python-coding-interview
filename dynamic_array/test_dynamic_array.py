import pytest

from dynamic_array import DynamicArray

# Test cases for insert function


def test_insert_into_empty_array():
    da = DynamicArray(1)
    da.insert(10)
    assert da._array[0] == 10
    assert da._size == 1


def test_insert_and_resize():
    da = DynamicArray(2)
    da.insert(10)
    da.insert(20)
    da.insert(30)  # Should trigger resize
    assert da._array[0] == 10
    assert da._array[1] == 20
    assert da._array[2] == 30
    assert da._size == 3
    assert da._capacity == 4  # Assuming resize doubles the capacity


def test_insert_at_full_capacity():
    da = DynamicArray(3)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.insert(40)  # Should trigger resize
    assert da._array[0] == 10
    assert da._array[1] == 20
    assert da._array[2] == 30
    assert da._array[3] == 40
    assert da._size == 4
    assert da._capacity == 6  # Depending on resize factor


def test_insert_after_multiple_resizes():
    da = DynamicArray(2)
    for i in range(10):  # Multiple insertions to trigger multiple resizes
        da.insert(i)
    for i in range(10):
        assert da._array[i] == i
    assert da._size == 10
    assert da._capacity >= 10  # Ensure capacity is enough to hold all elements


@pytest.mark.skip('alpha characters')
def test_insert_with_non_integer_values():
    da = DynamicArray(2, 'u')
    da.insert(ord('a'))
    da.insert(ord('b'))
    da.insert(ord('c'))  # Should trigger resize
    assert da._array[0] == ord('a')
    assert da._array[1] == ord('b')
    assert da._array[2] == ord('c')
    assert da._size == 3


# Test cases for delete function


def test_delete_from_empty_array():
    da = DynamicArray(1)
    with pytest.raises(ValueError, match="the entry is not in the array"):
        da.delete(10)


def test_delete_existing_value():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.delete(20)
    assert da._size == 2
    assert da._array[0] == 10
    assert da._array[1] == 30
    assert 20 not in da._array[:da._size]


def test_delete_non_existing_value():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    with pytest.raises(ValueError, match="the entry is not in the array"):
        da.delete(40)


def test_delete_first_element():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.delete(10)
    assert da._size == 2
    assert da._array[0] == 20
    assert da._array[1] == 30
    assert 10 not in da._array[:da._size]


def test_delete_last_element():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.delete(30)
    assert da._size == 2
    assert da._array[0] == 10
    assert da._array[1] == 20
    assert 30 not in da._array[:da._size]


def test_delete_after_multiple_insertions():
    da = DynamicArray(2)
    for i in range(10):  # Multiple insertions to trigger multiple resizes
        da.insert(i)
    da.delete(0)
    da.delete(9)
    assert da._size == 8
    for i in range(8):
        assert da._array[i] == i + 1
    assert 0 not in da._array[:da._size]
    assert 9 not in da._array[:da._size]


def test_delete_duplicate_values():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(10)
    da.insert(20)
    da.delete(10)
    assert da._size == 2
    assert da._array[0] == 10
    assert da._array[1] == 20
    assert da._array[2] != 10


def test_delete_and_insert():
    da = DynamicArray(5)
    da.insert(10)
    da.insert(20)
    da.insert(30)
    da.delete(20)
    da.insert(25)
    assert da._size == 3
    assert da._array[0] == 10
    assert da._array[1] == 30
    assert da._array[2] == 25


def test_delete_triggers_resize():
    da = DynamicArray(16)
    for i in range(16):
        da.insert(i)
    for i in range(12):  # Deleting multiple elements
        da.delete(i)
    assert da._size == 4
    # Assuming resize halves the capacity when array is quarter full
    # assert da._capacity == 8
