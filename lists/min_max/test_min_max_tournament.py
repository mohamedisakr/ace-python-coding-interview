import pytest
from min_max_tournament import min_max_arr_tournamtent
from min_max_iterative import min_max_arr_iterative


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_single_element(func):
    if func == min_max_arr_tournamtent:
        assert func([5], 0, 0) == (5, 5)
    else:
        assert func([5]) == (5, 5)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_two_elements(func):
    if func == min_max_arr_tournamtent:
        assert func([3, 8], 0, 1) == (3, 8)
    else:
        assert func([3, 8]) == (3, 8)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_multiple_elements(func):
    if func == min_max_arr_tournamtent:
        assert func([1, 2, 3, 4, 5], 0, 4) == (1, 5)
    else:
        assert func([1, 2, 3, 4, 5]) == (1, 5)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_unsorted_array(func):
    if func == min_max_arr_tournamtent:
        assert func([4, 2, 9, 6, 1], 0, 4) == (1, 9)
    else:
        assert func([4, 2, 9, 6, 1]) == (1, 9)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_all_same_elements(func):
    if func == min_max_arr_tournamtent:
        assert func([7, 7, 7, 7, 7], 0, 4) == (7, 7)
    else:
        assert func([7, 7, 7, 7, 7]) == (7, 7)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_negative_elements(func):
    if func == min_max_arr_tournamtent:
        assert func([-3, -1, -7, -5], 0, 3) == (-7, -1)
    else:
        assert func([-3, -1, -7, -5]) == (-7, -1)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_mixed_positive_and_negative(func):
    if func == min_max_arr_tournamtent:
        assert func([-10, 5, -2, 4, 1], 0, 4) == (-10, 5)
    else:
        assert func([-10, 5, -2, 4, 1]) == (-10, 5)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_large_range(func):
    if func == min_max_arr_tournamtent:
        assert func([1000, -1000, 0, 500, -500], 0, 4) == (-1000, 1000)
    else:
        assert func([1000, -1000, 0, 500, -500]) == (-1000, 1000)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_large_array(func):
    large_array = list(range(100000))
    if func == min_max_arr_tournamtent:
        assert func(large_array, 0, 99999) == (0, 99999)
    else:
        assert func(large_array) == (0, 99999)


@pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
def test_empty_array(func):
    with pytest.raises(ValueError):
        if func == min_max_arr_tournamtent:
            func([], 0, 0)
        else:
            func([])
# @pytest.mark.parametrize("func", [min_max_arr_tournamtent, min_max_arr_iterative])
# def test_empty_array(func):
#     with pytest.raises(ValueError):
#         if func == min_max_arr_tournamtent:
#             func([], 0, 0)
#         else:
#             func([])

# To run the tests, use the command:
# pytest your_test_file.py
