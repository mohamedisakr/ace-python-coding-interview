import unittest
from .second_max import find_second_max


class TestFindSecondMax(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_second_max([9, 2, 3, 6]), 6)

    def test_sorted_array(self):
        self.assertEqual(find_second_max([1, 2, 3, 4, 5]), 4)

    def test_reverse_sorted(self):
        self.assertEqual(find_second_max([5, 4, 3, 2, 1]), 4)

    def test_with_duplicates(self):
        self.assertEqual(find_second_max([5, 5, 4, 4, 3]), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_second_max([-10, -20, -30]), -20)

    def test_mixed_signs(self):
        self.assertEqual(find_second_max([-1, 0, 1]), 0)

    def test_large_input(self):
        arr = list(range(10000))
        self.assertEqual(find_second_max(arr), 9998)

    def test_invalid_case(self):
        with self.assertRaises(ValueError):
            find_second_max([5, 5, 5])


if __name__ == "__main__":
    unittest.main()
