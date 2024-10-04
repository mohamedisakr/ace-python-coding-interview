import unittest

from .two_numbers_k import find_sum


class TestFindSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_sum([1, 2, 3, 4, 5], 9), [4, 5])

    def test_negative_numbers(self):
        self.assertEqual(find_sum([-1, -2, -3, -4, -5], -8), [-3, -5])

    def test_mixed_numbers(self):
        self.assertEqual(find_sum([-1, 2, 3, -4, 5], 1), [-1, 2])

    def test_no_pair(self):
        self.assertIsNone(find_sum([1, 2, 3, 4, 5], 10))

    def test_empty_list(self):
        self.assertIsNone(find_sum([], 5))

    def test_single_element(self):
        self.assertIsNone(find_sum([1], 1))

    def test_duplicates(self):
        self.assertEqual(find_sum([1, 2, 3, 2, 4], 4), [1, 3])

    def test_large_numbers(self):
        self.assertEqual(
            find_sum([1000000, 500000, -1500000], -500000), [1000000, -1500000])

    def test_zero_sum(self):
        self.assertEqual(find_sum([0, 1, 2, -1], 0), [1, -1])

    # ------------ additional test cases -------


def find_sum(lst, k):
    seen = {}
    for number in lst:
        complement = k - number
        if complement in seen:
            return [complement, number]
        seen[number] = True
    return None  # Return None if no pair is found


class TestFindSum(unittest.TestCase):

    # Existing test cases
    def test_positive_numbers(self):
        self.assertEqual(find_sum([1, 2, 3, 4, 5], 9), [4, 5])

    def test_negative_numbers(self):
        self.assertEqual(find_sum([-1, -2, -3, -4, -5], -8), [-3, -5])

    def test_mixed_numbers(self):
        self.assertEqual(find_sum([-1, 2, 3, -4, 5], 1), [-1, 2])

    def test_no_pair(self):
        self.assertIsNone(find_sum([1, 2, 3, 4, 5], 10))

    def test_empty_list(self):
        self.assertIsNone(find_sum([], 5))

    def test_single_element(self):
        self.assertIsNone(find_sum([1], 1))

    def test_duplicates(self):
        self.assertEqual(find_sum([1, 2, 3, 2, 4], 4), [1, 3])

    def test_large_numbers(self):
        self.assertEqual(
            find_sum([1000000, 500000, -1500000], -500000), [1000000, -1500000])

    def test_zero_sum(self):
        self.assertEqual(find_sum([0, 1, 2, -1], 0), [1, -1])

    # ---------- Additional test cases ----------
    def test_all_elements_zero(self):
        self.assertEqual(find_sum([0, 0, 0, 0], 0), [0, 0])

    def test_sum_with_zero(self):
        self.assertEqual(find_sum([1, 2, 3, -3], 0), [3, -3])

    def test_negative_target_sum(self):
        self.assertEqual(find_sum([1, 2, 3, -4], -1), [3, -4])

    def test_large_positive_and_negative_numbers(self):
        self.assertEqual(
            find_sum([1000000, -1000000, 500000, -500000], 0), [1000000, -1000000])

    def test_non_integer_numbers(self):
        self.assertEqual(find_sum([1.1, 2.2, 3.3, 4.4], 5.5), [2.2, 3.3])

    def test_repeated_pairs(self):
        self.assertEqual(find_sum([1, 1, 2, 2, 3, 3], 4), [2, 2])


if __name__ == '__main__':
    unittest.main()
