import unittest
from .rearrange_negative_positive_partitioning import rearrange_in_place


class TestRearrangeInPlace(unittest.TestCase):
    def test_basic_case(self):
        arr = [10, -1, 20, 4, 5, -9, -6]
        rearrange_in_place(arr)
        self.assertEqual(arr[:3], [-1, -9, -6])
        self.assertCountEqual(arr[3:], [10, 20, 4, 5])

    def test_all_negatives(self):
        arr = [-5, -2, -9]
        rearrange_in_place(arr)
        self.assertEqual(arr, [-5, -2, -9])

    def test_all_positives(self):
        arr = [0, 1, 2]
        rearrange_in_place(arr)
        self.assertEqual(arr, [0, 1, 2])

    def test_mixed_with_zero(self):
        arr = [-1, 0, 2, -3]
        rearrange_in_place(arr)
        self.assertEqual(arr[:2], [-1, -3])
        self.assertCountEqual(arr[2:], [0, 2])

    def test_empty_array(self):
        arr = []
        rearrange_in_place(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [-1]
        rearrange_in_place(arr)
        self.assertEqual(arr, [-1])


if __name__ == "__main__":
    unittest.main()
