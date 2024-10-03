# Third party imports
import math
import unittest

# Local application imports
from .remove_even_in_place import remove_even


class TestRemoveEvenEdgeCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_all_odd_numbers(self):
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_numbers(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_even_number(self):
        self.assertEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        self.assertEqual(remove_even([1]), [1])

    def test_large_numbers(self):
        self.assertEqual(remove_even([1000000000, 1000000001]), [1000000001])

    def test_negative_numbers(self):
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_zero_in_list(self):
        self.assertEqual(remove_even([0, 1, 2, 3]), [1, 3])

    def test_repeated_elements(self):
        self.assertEqual(remove_even([2, 2, 2, 2]), [])
        self.assertEqual(remove_even([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(remove_even([1, 2, 1, 2]), [1, 1])

    def test_floating_point_numbers(self):
        self.assertEqual(remove_even([1.0, 2.0, 3.0, 4.0]), [1.0, 3.0])

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            remove_even([1, 'two', 3, 'four'])

    def test_large_range(self):
        large_list = list(range(1000000))
        expected_result = [x for x in large_list if x % 2 != 0]
        self.assertEqual(remove_even(large_list), expected_result)

    def test_special_values(self):
        with self.assertRaises(TypeError):
            remove_even([1, None, 3, None])
        with self.assertRaises(TypeError):
            remove_even([1, math.nan, 3, math.nan])


if __name__ == "__main__":
    unittest.main()
