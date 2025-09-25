import unittest
from .rearrange_negative_positive import rearrange


class TestRearrange(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(
            rearrange([10, -1, 20, 4, 5, -9, -6]), [-1, -9, -6, 10, 20, 4, 5])

    def test_all_negatives(self):
        self.assertEqual(rearrange([-5, -2, -9]), [-5, -2, -9])

    def test_all_positives(self):
        self.assertEqual(rearrange([0, 1, 2]), [0, 1, 2])

    def test_mixed_with_zero(self):
        self.assertEqual(rearrange([-1, 0, 2, -3]), [-1, -3, 0, 2])

    def test_empty_array(self):
        self.assertEqual(rearrange([]), [])

    def test_single_element(self):
        self.assertEqual(rearrange([-1]), [-1])
        self.assertEqual(rearrange([0]), [0])

    def test_order_preservation(self):
        self.assertEqual(rearrange([-2, -1, 3, 2]), [-2, -1, 3, 2])


if __name__ == "__main__":
    unittest.main()
