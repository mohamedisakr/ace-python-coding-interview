import pytest
from cycle_rotate import cyclic_rotate


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_single_element(func):
    assert func([5]) == [5]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_two_elements(func):
    assert func([1, 2]) == [2, 1]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_multiple_elements(func):
    assert func([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_unsorted_array(func):
    assert func([4, 2, 3, 1, 5]) == [5, 4, 2, 3, 1]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_all_same_elements(func):
    assert func([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_negative_elements(func):
    assert func([-1, -2, -3, -4, -5]) == [-5, -1, -2, -3, -4]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_mixed_positive_and_negative(func):
    assert func([10, -5, 3, -2, 0]) == [0, 10, -5, 3, -2]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_large_array(func):
    large_array = list(range(100000))
    expected_array = [99999] + list(range(99999))
    assert func(large_array) == expected_array


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_empty_array(func):
    assert func([]) == []

# ------------ Additional Test Cases -----------------


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_array_with_zero(func):
    assert func([1, 0, 3, 4, 5]) == [5, 1, 0, 3, 4]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_array_with_duplicates(func):
    assert func([1, 2, 2, 3, 3, 4, 4, 5]) == [5, 1, 2, 2, 3, 3, 4, 4]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_array_with_floats(func):
    assert func([1.1, 2.2, 3.3, 4.4, 5.5]) == [5.5, 1.1, 2.2, 3.3, 4.4]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_array_with_large_numbers(func):
    assert func([1000000, 999999, 1000001]) == [1000001, 1000000, 999999]


@pytest.mark.parametrize("func", [cyclic_rotate])
def test_array_with_positive_and_negative_zero(func):
    assert func([0, -0, 1, -1, 2, -2]) == [-2, 0, -0, 1, -1, 2]
