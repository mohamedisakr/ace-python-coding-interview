from unittest import TestCase, main
from .sorted_max_min_list import max_min


class TestMaxMinInPlace(TestCase):

    # -------- my 2 test cases ---------
    def test_first_case(self):
        self.assertEqual(max_min([1, 2, 3, 4, 5]), [5, 1, 4, 2, 3])

    def test_second_case(self):
        self.assertEqual(max_min([1, 2, 3, 4, 5, 6, 7]), [7, 1, 6, 2, 5, 3, 4])
    # -----------------------------------

    def test_empty_list(self):
        self.assertEqual(max_min([]), [])

    def test_single_element(self):
        self.assertEqual(max_min([1]), [1])

    def test_two_elements(self):
        self.assertEqual(max_min([1, 2]), [2, 1])

    def test_three_elements(self):
        self.assertEqual(max_min([1, 2, 3]), [3, 1, 2])

    def test_even_number_of_elements(self):
        self.assertEqual(max_min([1, 2, 3, 4]), [4, 1,  3, 2])

    def test_odd_number_of_elements(self):
        self.assertEqual(max_min([1, 2, 3, 4, 5]), [5, 1, 4, 2, 3])

    def test_all_elements_same(self):
        self.assertEqual(max_min([2, 2, 2, 2]), [2, 2, 2, 2])

    def test_large_numbers(self):
        self.assertEqual(max_min([1000, 2000, 3000, 4000]), [
                         4000, 1000, 3000, 2000])

    def test_negative_numbers(self):
        self.assertEqual(
            max_min([-3, -2, -1, 0, 1, 2, 3]), [3, -3, 2, -2, 1, -1, 0])

    def test_mixed_numbers(self):
        self.assertEqual(max_min([-10, -5, 0, 5, 10]), [10, -10, 5, -5, 0])

    def test_large_list(self):
        arr = list(range(1, 101))
        expected = []
        for i in range(50):
            expected.append(arr[99 - i])
            expected.append(arr[i])
        self.assertEqual(max_min(arr), expected)

    # ------ other test cases -------

    # def test_already_alternating(self):
    #     self.assertEqual(max_min(
    #         [1, 6, 2, 5, 3, 4]), [1, 6, 2, 5, 3, 4])

    # def test_reverse_sorted(self):
    #     self.assertEqual(max_min(
    #         [6, 5, 4, 3, 2, 1]), [6, 1, 5, 2, 4, 3])

    def test_duplicates(self):
        self.assertEqual(max_min(
            [1, 2, 2, 3, 3, 4]), [4, 1, 3, 2, 3, 2])

    def test_zeroes(self):
        self.assertEqual(max_min(
            [0, 0, 1, 1, 2, 2]), [2, 0, 2, 0, 1, 1])

    def test_large_range(self):
        self.assertEqual(max_min(
            [-1000, -500, 0, 500, 1000]), [1000, -1000, 500, -500, 0])

    def test_floating_point(self):
        self.assertEqual(max_min(
            [1.1, 2.2, 3.3, 4.4]), [4.4, 1.1, 3.3, 2.2])

    def test_mixed_data_types(self):
        self.assertEqual(max_min([1, 2.2, 3, 4.4]), [4.4, 1, 3,  2.2])


if __name__ == '__main__':
    main()
