import unittest
from .right_rotate import right_rotate


class TestRightRotate(unittest.TestCase):
    def test_basic_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])

    def test_zero_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3], 0), [1, 2, 3])

    def test_full_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3], 3), [1, 2, 3])

    def test_rotation_greater_than_length(self):
        self.assertEqual(right_rotate([1, 2, 3], 5), [2, 3, 1])

    def test_empty_array(self):
        self.assertEqual(right_rotate([], 3), [])

    def test_single_element(self):
        self.assertEqual(right_rotate([42], 10), [42])


if __name__ == "__main__":
    unittest.main()
