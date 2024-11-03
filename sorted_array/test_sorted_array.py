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

# Test cases for search function


def test_search_in_empty_array():
    sa = SortedArray(5)
    assert sa.linear_search(10) is None


def test_search_existing_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    assert sa.linear_search(20) == 1
    assert sa.linear_search(10) == 0
    assert sa.linear_search(30) == 2


def test_search_non_existing_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    assert sa.linear_search(40) is None


def test_search_first_element():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    assert sa.linear_search(10) == 0


def test_search_last_element():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    assert sa.linear_search(30) == 2


def test_search_after_deletions():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa._array[1] = sa._array[2]  # Simulate deletion by shifting left
    sa._size -= 1
    assert sa.linear_search(20) is None
    assert sa.linear_search(30) == 1


def test_search_duplicate_values():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(10)
    sa.insert(20)
    # Ensure one of the duplicates is found
    assert sa.linear_search(10) == 0 or sa.linear_search(10) == 1


@pytest.mark.skip('non integer')
def test_search_non_integer_values():
    sa = SortedArray(5, 'u')
    sa.insert(ord('a'))
    sa.insert(ord('b'))
    sa.insert(ord('c'))
    assert sa.linear_search(ord('b')) == 1

# Test cases for delete function


def test_delete_from_empty_array():
    sa = SortedArray(5)
    with pytest.raises(ValueError, match="the entry is not in the array"):
        sa.delete(10)


def test_delete_existing_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.delete(20)
    assert sa._size == 2
    assert sa._array[0] == 10
    assert sa._array[1] == 30
    assert sa.linear_search(20) is None


def test_delete_non_existing_value():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    with pytest.raises(ValueError, match="the entry is not in the array"):
        sa.delete(40)


def test_delete_first_element():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.delete(10)
    assert sa._size == 2
    assert sa._array[0] == 20
    assert sa._array[1] == 30
    assert sa.linear_search(10) is None


def test_delete_last_element():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.delete(30)
    assert sa._size == 2
    assert sa._array[0] == 10
    assert sa._array[1] == 20
    assert sa.linear_search(30) is None


def test_delete_after_insertions_and_deletions():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(20)
    sa.insert(30)
    sa.delete(20)
    sa.insert(25)
    sa.delete(10)
    assert sa._size == 2
    assert sa._array[0] == 25
    assert sa._array[1] == 30
    assert sa.linear_search(10) is None
    assert sa.linear_search(20) is None
    assert sa.linear_search(25) == 0
    assert sa.linear_search(30) == 1


def test_delete_duplicate_values():
    sa = SortedArray(5)
    sa.insert(10)
    sa.insert(10)
    sa.insert(20)
    sa.delete(10)
    assert sa._size == 2
    assert sa._array[0] == 10
    assert sa._array[1] == 20
    # Ensure one of the duplicates is found
    assert sa.linear_search(10) == 0 or sa.linear_search(10) == 1
