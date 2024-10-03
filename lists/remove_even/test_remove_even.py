# Third party imports
import math
import unittest

# Local application imports
from .remove_even_in_place import remove_even


class TestRemoveEvenEdgeCases(unittest.TestCase):
    def setUp(self):
        """Set up any state specific to the execution of the given class."""
        self.test_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        """Clean up any state that was set up for the test."""
        del self.test_list

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(remove_even([]), [])

    def test_all_even_numbers(self):
        """Test that a list with all even numbers returns an empty list."""
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_all_odd_numbers(self):
        """Test that a list with all odd numbers returns the same list."""
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_numbers(self):
        """Test that a list with mixed even and odd numbers returns only odd numbers."""
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_even_number(self):
        """Test that a list with a single even number returns an empty list."""
        self.assertEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        """Test that a list with a single odd number returns the same list."""
        self.assertEqual(remove_even([1]), [1])

    def test_large_numbers(self):
        """Test that a list with large numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1000000000, 1000000001]), [1000000001])

    def test_negative_numbers(self):
        """Test that a list with negative numbers correctly removes even numbers."""
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_zero_in_list(self):
        """Test that a list with zero correctly removes zero."""
        self.assertEqual(remove_even([0, 1, 2, 3]), [1, 3])

    def test_repeated_elements(self):
        """Test that a list with repeated elements correctly removes even numbers."""
        self.assertEqual(remove_even([2, 2, 2, 2]), [])
        self.assertEqual(remove_even([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(remove_even([1, 2, 1, 2]), [1, 1])

    def test_floating_point_numbers(self):
        """Test that a list with floating point numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1.0, 2.0, 3.0, 4.0]), [1.0, 3.0])

    def test_mixed_data_types(self):
        """Test that a list with mixed data types raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, 'two', 3, 'four'])

    def test_large_range(self):
        """Test that a large range of numbers correctly removes even numbers."""
        large_list = list(range(1000000))
        expected_result = [x for x in large_list if x % 2 != 0]
        self.assertEqual(remove_even(large_list), expected_result)

    def test_special_values(self):
        """Test that a list with special values (None, NaN) raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, None, 3, None])
        with self.assertRaises(TypeError):
            remove_even([1, math.nan, 3, math.nan])


if __name__ == "__main__":
    unittest.main()

'''
class TestRemoveEvenEdgeCases(unittest.TestCase):
    def setUp(self):
        """Set up any state specific to the execution of the given class."""
        self.test_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        """Clean up any state that was set up for the test."""
        del self.test_list

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(remove_even([]), [])

    def test_all_even_numbers(self):
        """Test that a list with all even numbers returns an empty list."""
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_all_odd_numbers(self):
        """Test that a list with all odd numbers returns the same list."""
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_numbers(self):
        """Test that a list with mixed even and odd numbers returns only odd numbers."""
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_even_number(self):
        """Test that a list with a single even number returns an empty list."""
        self.assertEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        """Test that a list with a single odd number returns the same list."""
        self.assertEqual(remove_even([1]), [1])

    def test_large_numbers(self):
        """Test that a list with large numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1000000000, 1000000001]), [1000000001])

    def test_negative_numbers(self):
        """Test that a list with negative numbers correctly removes even numbers."""
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_zero_in_list(self):
        """Test that a list with zero correctly removes zero."""
        self.assertEqual(remove_even([0, 1, 2, 3]), [1, 3])

    def test_repeated_elements(self):
        """Test that a list with repeated elements correctly removes even numbers."""
        self.assertEqual(remove_even([2, 2, 2, 2]), [])
        self.assertEqual(remove_even([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(remove_even([1, 2, 1, 2]), [1, 1])

    def test_floating_point_numbers(self):
        """Test that a list with floating point numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1.0, 2.0, 3.0, 4.0]), [1.0, 3.0])

    def test_mixed_data_types(self):
        """Test that a list with mixed data types raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, 'two', 3, 'four'])

    def test_large_range(self):
        """Test that a large range of numbers correctly removes even numbers."""
        large_list = list(range(1000000))
        expected_result = [x for x in large_list if x % 2 != 0]
        self.assertEqual(remove_even(large_list), expected_result)

    def test_special_values(self):
        """Test that a list with special values (None, NaN) raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, None, 3, None])
        with self.assertRaises(TypeError):
            remove_even([1, math.nan, 3, math.nan])


if __name__ == "__main__":
    unittest.main()
'''

'''
class TestRemoveEvenEdgeCases(unittest.TestCase):
    def setUp(self):
        """Set up any state specific to the execution of the given class."""
        self.test_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        """Clean up any state that was set up for the test."""
        del self.test_list

    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(remove_even([]), [])

    def test_all_even_numbers(self):
        """Test that a list with all even numbers returns an empty list."""
        self.assertEqual(remove_even([2, 4, 6, 8, 10]), [])

    def test_all_odd_numbers(self):
        """Test that a list with all odd numbers returns the same list."""
        self.assertEqual(remove_even([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_mixed_numbers(self):
        """Test that a list with mixed even and odd numbers returns only odd numbers."""
        self.assertEqual(remove_even([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_single_even_number(self):
        """Test that a list with a single even number returns an empty list."""
        self.assertEqual(remove_even([2]), [])

    def test_single_odd_number(self):
        """Test that a list with a single odd number returns the same list."""
        self.assertEqual(remove_even([1]), [1])

    def test_large_numbers(self):
        """Test that a list with large numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1000000000, 1000000001]), [1000000001])

    def test_negative_numbers(self):
        """Test that a list with negative numbers correctly removes even numbers."""
        self.assertEqual(remove_even([-1, -2, -3, -4]), [-1, -3])

    def test_zero_in_list(self):
        """Test that a list with zero correctly removes zero."""
        self.assertEqual(remove_even([0, 1, 2, 3]), [1, 3])

    def test_repeated_elements(self):
        """Test that a list with repeated elements correctly removes even numbers."""
        self.assertEqual(remove_even([2, 2, 2, 2]), [])
        self.assertEqual(remove_even([1, 1, 1, 1]), [1, 1, 1, 1])
        self.assertEqual(remove_even([1, 2, 1, 2]), [1, 1])

    def test_floating_point_numbers(self):
        """Test that a list with floating point numbers correctly removes even numbers."""
        self.assertEqual(remove_even([1.0, 2.0, 3.0, 4.0]), [1.0, 3.0])

    def test_mixed_data_types(self):
        """Test that a list with mixed data types raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, 'two', 3, 'four'])

    def test_large_range(self):
        """Test that a large range of numbers correctly removes even numbers."""
        large_list = list(range(1000000))
        expected_result = [x for x in large_list if x % 2 != 0]
        self.assertEqual(remove_even(large_list), expected_result)

    def test_special_values(self):
        """Test that a list with special values (None, NaN) raises a TypeError."""
        with self.assertRaises(TypeError):
            remove_even([1, None, 3, None])
        with self.assertRaises(TypeError):
            remove_even([1, math.nan, 3, math.nan])


if __name__ == "__main__":
    unittest.main()

'''

'''
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
'''
