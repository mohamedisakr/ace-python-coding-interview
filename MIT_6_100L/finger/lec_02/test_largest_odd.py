from unittest import TestCase, main
from .largest_odd import largest_odd


class TestLargestOdd(TestCase):
    def test_valid_with_odds(self):
        nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
        self.assertEqual(largest_odd(nums), 9)

    def test_valid_no_odds(self):
        nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        self.assertIsNone(largest_odd(nums))

    def test_all_odds(self):
        nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.assertEqual(largest_odd(nums), 19)

    def test_duplicates(self):
        nums = [1, 3, 3, 3, 5, 5, 5, 7, 7, 7]
        self.assertEqual(largest_odd(nums), 7)

    def test_negative_odds(self):
        nums = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19]
        self.assertEqual(largest_odd(nums), -1)

    def test_mixed_signs(self):
        nums = [-10, -3, 0, 2, 4, 6, 8, 10, 11, 13]
        self.assertEqual(largest_odd(nums), 13)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            largest_odd([1, 2, 3])  # Too short

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            largest_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, "10"])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            largest_odd([])


if __name__ == '__main__':
    main()
