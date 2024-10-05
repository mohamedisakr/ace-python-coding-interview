from unittest import TestCase, main
from .list_products_all_elements import find_product


class TestFindProduct(TestCase):
    def test_general_case(self):
        self.assertEqual(find_product([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(find_product([2, -3, 4, -5]), [60, -40, 30, -24])

    def test_with_zero(self):
        self.assertEqual(find_product([1, 0, 3, 4]), [0, 12, 0, 0])
        self.assertEqual(find_product([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_all_ones(self):
        self.assertEqual(find_product([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_single_element(self):
        self.assertEqual(find_product([5]), [1])

    def test_two_elements(self):
        self.assertEqual(find_product([3, 7]), [7, 3])

    def test_negative_numbers(self):
        self.assertEqual(find_product([-1, -2, -3, -4]), [-24, -12, -8, -6])

    def test_large_numbers(self):
        self.assertEqual(find_product([1000, 2000, 3000, 4000]), [
                         24000000000, 12000000000, 8000000000, 6000000000])

    def test_empty_list(self):
        self.assertEqual(find_product([]), [])


if __name__ == "__main__":
    main()
