import unittest
from .binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_list_found(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_single_element_list_not_found(self):
        self.assertEqual(binary_search([1], 2), -1)

    def test_multiple_elements_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_multiple_elements_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_duplicates(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 3], 2), 2)

    # ---------------- other test cases  ----------------#

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_list_found(self):
        self.assertEqual(binary_search([1], 1), 0)

    def test_single_element_list_not_found(self):
        self.assertEqual(binary_search([1], 2), -1)

    def test_multiple_elements_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_multiple_elements_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_first_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_last_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_duplicates(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 3], 2), 2)

    def test_negative_numbers(self):
        self.assertEqual(binary_search([-5, -4, -3, -2, -1], -3), 2)

    def test_all_identical_elements_found(self):
        self.assertEqual(binary_search([2, 2, 2, 2, 2], 2), 2)

    def test_all_identical_elements_not_found(self):
        self.assertEqual(binary_search([2, 2, 2, 2, 2], 3), -1)

    def test_middle_element(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_large_list(self):
        large_list = list(range(1000000))
        self.assertEqual(binary_search(large_list, 999999), 999999)

    def test_floating_point_numbers(self):
        self.assertEqual(binary_search([1.1, 2.2, 3.3, 4.4, 5.5], 3.3), 2)


if __name__ == '__main__':
    unittest.main()
