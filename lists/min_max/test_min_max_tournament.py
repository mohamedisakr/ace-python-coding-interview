import pytest

from min_max_tournament import min_max_arr  # Make sure to import your function


def test_single_element():
    assert min_max_arr([5], 0, 0) == (5, 5)


def test_two_elements():
    assert min_max_arr([3, 8], 0, 1) == (3, 8)


def test_multiple_elements():
    assert min_max_arr([1, 2, 3, 4, 5], 0, 4) == (1, 5)


def test_unsorted_array():
    assert min_max_arr([4, 2, 9, 6, 1], 0, 4) == (1, 9)


def test_all_same_elements():
    assert min_max_arr([7, 7, 7, 7, 7], 0, 4) == (7, 7)


def test_negative_elements():
    assert min_max_arr([-3, -1, -7, -5], 0, 3) == (-7, -1)


def test_mixed_positive_and_negative():
    assert min_max_arr([-10, 5, -2, 4, 1], 0, 4) == (-10, 5)


def test_large_range():
    assert min_max_arr([1000, -1000, 0, 500, -500], 0, 4) == (-1000, 1000)


def test_large_array():
    assert min_max_arr(list(range(100000)), 0, 99999) == (0, 99999)


def test_empty_array():
    with pytest.raises(IndexError):
        min_max_arr([], 0, 0)

# To run the tests, use the command:
# pytest your_test_file.py
