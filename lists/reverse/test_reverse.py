import pytest
from naive import reverse_naive
from in_place import reverse_in_place


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_single_element(func):
    assert func([5]) == [5]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_two_elements(func):
    assert func([1, 2]) == [2, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_multiple_elements(func):
    assert func([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_unsorted_array(func):
    assert func([4, 2, 3, 1, 5]) == [5, 1, 3, 2, 4]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_all_same_elements(func):
    assert func([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_negative_elements(func):
    assert func([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_mixed_positive_and_negative(func):
    assert func([10, -5, 3, -2, 0]) == [0, -2, 3, -5, 10]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_large_array(func):
    large_array = list(range(100000))
    reversed_array = list(range(99999, -1, -1))
    assert func(large_array) == reversed_array


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_empty_array(func):
    with pytest.raises(ValueError):
        func([])


# -------- other test cases ----------

# Implementations

def reverse_naive(arr):
    if not arr:
        raise ValueError("List is empty")
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[n - i - 1]
    return temp


def reverse_in_place(arr):
    if not arr:
        raise ValueError("List is empty")
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    return arr

# Test Cases


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_single_element(func):
    assert func([5]) == [5]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_two_elements(func):
    assert func([1, 2]) == [2, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_multiple_elements(func):
    assert func([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_unsorted_array(func):
    assert func([4, 2, 3, 1, 5]) == [5, 1, 3, 2, 4]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_all_same_elements(func):
    assert func([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_negative_elements(func):
    assert func([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_mixed_positive_and_negative(func):
    assert func([10, -5, 3, -2, 0]) == [0, -2, 3, -5, 10]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_large_array(func):
    large_array = list(range(100000))
    reversed_array = list(range(99999, -1, -1))
    assert func(large_array) == reversed_array


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_empty_array(func):
    with pytest.raises(ValueError):
        func([])


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_odd_number_of_elements(func):
    assert func([1, 3, 5]) == [5, 3, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_array_with_zero(func):
    assert func([0, 1, 2, 3]) == [3, 2, 1, 0]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_array_with_floats(func):
    assert func([1.1, 2.2, 3.3]) == [3.3, 2.2, 1.1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_array_with_large_numbers(func):
    assert func([1000000, 999999, 1000001]) == [1000001, 999999, 1000000]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_array_with_duplicates(func):
    assert func([1, 2, 2, 3]) == [3, 2, 2, 1]


@pytest.mark.parametrize("func", [reverse_naive, reverse_in_place])
def test_array_with_mixed_types(func):
    assert func([1, 'a', 2, 'b']) == ['b', 2, 'a', 1]
