import unittest
from .merge_2_sorted_intro import merge_lists


class TestMergeLists(unittest.TestCase):
    def test_basic_merge(self):
        self.assertEqual(merge_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_empty_first(self):
        self.assertEqual(merge_lists([], [1, 2, 3]), [1, 2, 3])

    def test_empty_second(self):
        self.assertEqual(merge_lists([1, 2, 3], []), [1, 2, 3])

    def test_both_empty(self):
        self.assertEqual(merge_lists([], []), [])

    def test_duplicates(self):
        self.assertEqual(merge_lists([1, 2, 2], [2, 3]), [1, 2, 2, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(merge_lists([-3, -1, 0], [-2, 1]), [-3, -2, -1, 0, 1])


if __name__ == "__main__":
    unittest.main()
