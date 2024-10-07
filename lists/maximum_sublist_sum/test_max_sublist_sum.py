import unittest
from unittest import TestCase, main
from .max_sublist_sum import find_max_sum_sublist


class TestMaxSubarraySum(TestCase):
    def test_single_element(self):
        self.assertEqual(find_max_sum_sublist([5]), 5)
        self.assertEqual(find_max_sum_sublist([-5]), -5)
        self.assertEqual(find_max_sum_sublist([0]), 0)

    def test_all_positive(self):
        self.assertEqual(find_max_sum_sublist([1, 2, 3, 4, 5]), 15)

    def test_all_negative(self):
        self.assertEqual(find_max_sum_sublist([-1, -2, -3, -4, -5]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(find_max_sum_sublist(
            [-2, -3, 4, -1, -2, 1, 5, -3]), 7)

    def test_mixed_with_zero(self):
        self.assertEqual(find_max_sum_sublist([0, -3, 5, -2, 0, 3, -1]), 6)

    def test_empty_array(self):
        self.assertEqual(find_max_sum_sublist([]), 0)

    def test_large_numbers(self):
        self.assertEqual(find_max_sum_sublist([1000000, -1, 1000000]), 1999999)

    def test_all_zeros(self):
        self.assertEqual(find_max_sum_sublist([0, 0, 0, 0]), 0)

    def test_alternating_positive_negative(self):
        self.assertEqual(find_max_sum_sublist([2, -1, 2, -1, 2, -1, 2]), 5)

    # --------------------------- additional test cases ---------------------------#

    # Additional boundary and edge cases

    def test_large_positive_negative_numbers(self):
        self.assertEqual(find_max_sum_sublist(
            [1000000000, -1000000000, 1000000000, -1000000000]), 1000000000)

    def test_single_large_positive_number(self):
        self.assertEqual(find_max_sum_sublist([1000000000]), 1000000000)

    def test_single_large_negative_number(self):
        self.assertEqual(find_max_sum_sublist([-1000000000]), -1000000000)

    def test_max_min_integer_values(self):
        self.assertEqual(find_max_sum_sublist(
            [2147483647, -2147483648, 2147483647]), 2147483647)

    def test_repeated_single_element(self):
        self.assertEqual(find_max_sum_sublist([1] * 1000), 1000)
        self.assertEqual(find_max_sum_sublist([-1] * 1000), -1)

    def test_alternating_large_positive_negative(self):
        self.assertEqual(find_max_sum_sublist(
            [1000000, -1000000] * 500), 1000000)

    def test_large_zeros_single_non_zero(self):
        self.assertEqual(find_max_sum_sublist([0] * 999 + [1]), 1)

    def test_increasing_decreasing_sequence(self):
        self.assertEqual(find_max_sum_sublist(
            list(range(1, 501)) + list(range(500, 0, -1))), 250500)


if __name__ == '__main__':
    main()
