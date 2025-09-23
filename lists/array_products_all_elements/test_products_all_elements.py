import unittest
from .products_all_elements import find_product


class TestFindProduct(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_product([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_with_zero(self):
        self.assertEqual(find_product([1, 0, 3, 4]), [0, 12, 0, 0])

    def test_with_multiple_zeros(self):
        self.assertEqual(find_product([0, 0, 3]), [0, 0, 0])

    def test_with_negative_numbers(self):
        self.assertEqual(find_product([-1, 2, -3]), [-6, 3, -2])

    def test_with_floats(self):
        self.assertEqual(find_product([1.0, 2.0, 3.0]), [6.0, 3.0, 2.0])

    # def test_with_single_element(self):
    #     with self.assertRaises(IndexError):
    #         find_product([5])  # Problem states array size ≥ 2

    def test_with_two_elements(self):
        self.assertEqual(find_product([2, 3]), [3, 2])

    # def test_large_input(self):
    #     arr = list(range(1, 101))  # [1, 2, ..., 100]
    #     result = find_product(arr)
    #     self.assertEqual(len(result), 100)
    #     self.assertEqual(result[0], prod(arr[1:]))
    #     self.assertEqual(result[-1], prod(arr[:-1]))


if __name__ == "__main__":
    unittest.main()
