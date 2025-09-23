import unittest
from .first_unique import find_first_unique


class TestFindFirstUnique(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_first_unique([9, 2, 3, 2, 6, 6]), 9)

    def test_multiple_uniques(self):
        self.assertEqual(find_first_unique([4, 5, 6, 4, 5]), 6)

    def test_no_unique(self):
        self.assertIsNone(find_first_unique([1, 1, 2, 2]))

    def test_single_element(self):
        self.assertEqual(find_first_unique([42]), 42)

    def test_empty_array(self):
        self.assertIsNone(find_first_unique([]))

    def test_negative_numbers(self):
        self.assertEqual(find_first_unique([-1, -2, -1, -3]), -2)

    def test_floats_and_integers(self):
        self.assertEqual(find_first_unique([1.1, 2, 1.1, 3]), 2)

    def test_large_input(self):
        arr = [i for i in range(1000)] + [999]  # 999 appears twice
        self.assertEqual(find_first_unique(arr), 0)


if __name__ == "__main__":
    unittest.main()
