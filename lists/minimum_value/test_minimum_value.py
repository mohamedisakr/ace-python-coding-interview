from unittest import TestCase, main
from .minimum_value import find_minimum


class TestFindMinimum(TestCase):

    def test_single_element(self):
        self.assertEqual(find_minimum([42]), 42,
                         "Failed on single element list")

    def test_all_positive(self):
        self.assertEqual(find_minimum(
            [3, 1, 4, 1, 5, 9]), 1, "Failed on all positive numbers")

    def test_all_negative(self):
        self.assertEqual(find_minimum(
            [-3, -1, -4, -1, -5, -9]), -9, "Failed on all negative numbers")

    def test_mixed_numbers(self):
        self.assertEqual(find_minimum(
            [3, -1, 4, -1, 5, -9]), -9, "Failed on mixed positive and negative numbers")

    def test_duplicates(self):
        self.assertEqual(find_minimum(
            [2, 2, 2, 2, 2]), 2, "Failed on list with all duplicates")

    def test_large_numbers(self):
        self.assertEqual(find_minimum(
            [1000000, 999999, 1000001]), 999999, "Failed on large numbers")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_minimum([])

    # ------- other test cases ---------#

    def test_large_list(self):
        large_list = list(range(1000000, 0, -1))
        self.assertEqual(find_minimum(large_list), 1, "Failed on large list")

    def test_list_with_zeroes(self):
        self.assertEqual(find_minimum(
            [0, 1, 2, 3, -1, 0]), -1, "Failed on list with zeroes")

    def test_floating_point_numbers(self):
        self.assertEqual(find_minimum(
            [1.5, 2.5, -1.5, 0.5]), -1.5, "Failed on floating point numbers")

    def test_repeated_minimum_values(self):
        self.assertEqual(find_minimum(
            [3, 1, 4, 1, 5, 1]), 1, "Failed on repeated minimum values")

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            find_minimum([1, 'a', 3])


if __name__ == '__main__':
    main()
