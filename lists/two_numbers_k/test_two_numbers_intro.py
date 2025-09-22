import unittest
from .two_numbers_intro import find_sum


class TestFindSum(unittest.TestCase):
    def test_pair_exists(self):
        self.assertTrue(find_sum([1, 4, 5, 3], 7))

    def test_no_pair(self):
        self.assertFalse(find_sum([1, 2, 3], 10))

    def test_duplicates(self):
        self.assertTrue(find_sum([5, 5], 10))

    def test_negative_numbers(self):
        self.assertTrue(find_sum([-1, -2, 3], 1))

    def test_empty_array(self):
        self.assertFalse(find_sum([], 5))

    def test_single_element(self):
        self.assertFalse(find_sum([5], 5))


if __name__ == "__main__":
    unittest.main()
