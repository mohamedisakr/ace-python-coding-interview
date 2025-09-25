import unittest
from .quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    def sort_and_check(self, input_arr, expected):
        arr = input_arr.copy()
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_basic_case(self):
        self.sort_and_check([3, 1, 4, 2], [1, 2, 3, 4])

    def test_already_sorted(self):
        self.sort_and_check([1, 2, 3, 4], [1, 2, 3, 4])

    def test_reverse_sorted(self):
        self.sort_and_check([4, 3, 2, 1], [1, 2, 3, 4])

    def test_with_duplicates(self):
        self.sort_and_check([3, 1, 2, 2, 3], [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.sort_and_check([-3, -1, -2], [-3, -2, -1])

    def test_mixed_signs(self):
        self.sort_and_check([0, -1, 1], [-1, 0, 1])

    def test_single_element(self):
        self.sort_and_check([42], [42])

    def test_empty_array(self):
        self.sort_and_check([], [])

    def test_large_input(self):
        arr = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        self.sort_and_check(arr, expected)


if __name__ == "__main__":
    unittest.main()
