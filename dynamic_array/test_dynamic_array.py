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
