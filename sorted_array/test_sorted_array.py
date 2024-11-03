import pytest
# from arrays.core import Array
from sorted_array import SortedArray

# Test cases for insert function


def test_insert_into_empty_array():
    sa = SortedArray(5)
    sa.insert(10)
    assert sa._array[0] == 10
    assert sa._size == 1


def test_insert_into_full_array():
    sa = SortedArray(3)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    with pytest.raises(ValueError, match="The array is already full"):
        sa.insert(40)


def test_insert_at_beginning():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(5)
    assert sa._array[0] == 5
    assert sa._array[1] == 10
    assert sa._array[2] == 20
    assert sa._size == 3


def test_insert_at_end():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.insert(40)
    assert sa._array[3] == 40
    assert sa._size == 4


def test_insert_in_middle():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(30)
    sa.insert(20)
    assert sa._array[0] == 10
    assert sa._array[1] == 20
    assert sa._array[2] == 30
    assert sa._size == 3


def test_insert_duplicate_values():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(10)
    assert sa._array[0] == 10
    assert sa._array[1] == 10
    assert sa._array[2] == 20
    assert sa._size == 3


def test_insert_max_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.insert(40)
    sa.insert(50)
    assert sa._array[4] == 50
    assert sa._size == 5


def test_insert_min_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.insert(5)
    assert sa._array[0] == 5
    assert sa._array[1] == 10
    assert sa._array[2] == 20
    assert sa._array[3] == 30
    assert sa._size == 4
