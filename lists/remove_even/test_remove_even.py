# Third party imports
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


if __name__ == "__main__":
    unittest.main()

'''
class TestRemoveEven(unittest.TestCase):
    def test_remove_even(self):
        self.assertEqual(remove_even([1, 2, 4, 5, 10, 6, 3]), [1, 5, 3])
        self.assertEqual(remove_even([2, 4, 6, 8]), [])
        self.assertEqual(remove_even([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(remove_even([]), [])
        self.assertEqual(remove_even([0, 2, 4, 6]), [])
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])


if __name__ == "__main__":
    unittest.main()
'''
