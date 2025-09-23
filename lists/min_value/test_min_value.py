import unittest
from .min_value import find_minimum


class TestFindMinimum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_minimum([3, 1, 4, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_minimum([-5, -2, -9, 0]), -9)

    def test_single_element(self):
        self.assertEqual(find_minimum([42]), 42)

    def test_sorted_array(self):
        self.assertEqual(find_minimum([1, 2, 3, 4]), 1)

    def test_reverse_sorted(self):
        self.assertEqual(find_minimum([4, 3, 2, 1]), 1)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_minimum([])


if __name__ == "__main__":
    unittest.main()
