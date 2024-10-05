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

    # --------- other test cases ---------

    def test_repeated_elements(self):
        self.assertEqual(find_product([2, 2, 2, 2]), [8, 8, 8, 8])

    def test_alternating_positive_negative(self):
        self.assertEqual(find_product([1, -1, 1, -1]), [1, -1, 1, -1])

    def test_large_list_size(self):
        large_list = list(range(1, 1001))
        expected_output = [1] * 1000
        product_all = 1
        for num in large_list:
            product_all *= num
        for i in range(1000):
            expected_output[i] = product_all // large_list[i]
        self.assertEqual(find_product(large_list), expected_output)

    def test_floating_point_numbers(self):
        self.assertEqual(find_product([1.5, 2.5, 3.5, 4.5]), [
                         39.375, 23.625, 16.875, 13.125])

    def test_mixed_integers_floats(self):
        self.assertEqual(find_product([1, 2.5, 3, 4.5]), [
                         33.75, 13.5, 11.25, 7.5])

    def test_large_small_numbers(self):
        self.assertEqual(find_product(
            [1e10, 1e-10, 1e10, 1e-10]), [1e-10, 1e10, 1e-10, 1e10])


if __name__ == "__main__":
    main()
