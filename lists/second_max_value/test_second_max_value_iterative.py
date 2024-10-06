from unittest import TestCase, main
from .second_max_value_iterative import find_second_maximum


class TestFindSecondMaximum(TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_second_maximum([]))

    def test_single_element_list(self):
        self.assertIsNone(find_second_maximum([5]))

    def test_two_elements_list(self):
        self.assertEqual(find_second_maximum([5, 10]), 5)
        self.assertEqual(find_second_maximum([10, 5]), 5)

    def test_all_elements_same(self):
        self.assertIsNone(find_second_maximum([5, 5, 5, 5]))

    def test_typical_case(self):
        self.assertEqual(find_second_maximum([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_maximum([5, 4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_second_maximum([-1, -2, -3, -4, -5]), -2)
        self.assertEqual(find_second_maximum([-5, -4, -3, -2, -1]), -2)

    def test_list_with_duplicates(self):
        self.assertEqual(find_second_maximum([1, 3, 3, 4, 5]), 4)
        self.assertEqual(find_second_maximum([5, 5, 4, 4, 3]), 4)

    def test_large_list(self):
        large_list = list(range(1000000))
        self.assertEqual(find_second_maximum(large_list), 999998)

    # ------ other test cases ------

    def test_empty_list(self):
        self.assertIsNone(find_second_maximum([]))

    def test_single_element_list(self):
        self.assertIsNone(find_second_maximum([5]))

    def test_two_elements_list(self):
        self.assertEqual(find_second_maximum([5, 10]), 5)
        self.assertEqual(find_second_maximum([10, 5]), 5)

    def test_all_elements_same(self):
        self.assertIsNone(find_second_maximum([5, 5, 5, 5]))

    def test_typical_case(self):
        self.assertEqual(find_second_maximum([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_maximum([5, 4, 3, 2, 1]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_second_maximum([-1, -2, -3, -4, -5]), -2)
        self.assertEqual(find_second_maximum([-5, -4, -3, -2, -1]), -2)

    def test_list_with_duplicates(self):
        self.assertEqual(find_second_maximum([1, 3, 3, 4, 5]), 4)
        self.assertEqual(find_second_maximum([5, 5, 4, 4, 3]), 4)

    def test_large_list(self):
        large_list = list(range(1000000))
        self.assertEqual(find_second_maximum(large_list), 999998)

    # Boundary and Edge Cases
    def test_minimum_length_list(self):
        self.assertEqual(find_second_maximum([1, 2]), 1)
        self.assertEqual(find_second_maximum([2, 1]), 1)

    def test_max_min_integers(self):
        self.assertEqual(find_second_maximum(
            [float('-inf'), float('inf')]), float('-inf'))
        self.assertEqual(find_second_maximum(
            [float('inf'), float('-inf')]), float('-inf'))

    def test_repeated_maximum_values(self):
        self.assertEqual(find_second_maximum([5, 5, 4, 4, 3]), 4)
        self.assertEqual(find_second_maximum([5, 5, 5, 4]), 4)

    def test_only_negative_numbers(self):
        self.assertEqual(find_second_maximum([-10, -20, -30, -40]), -20)
        self.assertEqual(find_second_maximum([-1, -1, -1, -2]), -2)

    def test_list_with_zeroes(self):
        self.assertEqual(find_second_maximum([0, 0, 1, 2]), 1)
        self.assertEqual(find_second_maximum([0, -1, -2, -3]), -2)

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(find_second_maximum([-1, 2, -3, 4]), 2)
        self.assertEqual(find_second_maximum([1, -2, 3, -4]), 1)


if __name__ == '__main__':
    main()
