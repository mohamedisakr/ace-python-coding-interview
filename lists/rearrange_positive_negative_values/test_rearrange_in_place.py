from unittest import TestCase, main
from .rearrange_in_place import rearrange


class TestRearrangeFunction(TestCase):

    # my test case
    def test_mix_positive_negative(self):
        self.assertEqual(
            rearrange([10, -1, 20, 4, 5, -9, -6]), [-1, -9, -6, 10, 20, 4, 5])

    def test_all_positive(self):
        self.assertEqual(rearrange([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_all_negative(self):
        self.assertEqual(rearrange([-1, -2, -3, -4]), [-1, -2, -3, -4])

    def test_mixed_values(self):
        self.assertEqual(
            rearrange([10, -1, 20, 4, 5, -9, -6]), [-1, -9, -6, 10, 20, 4, 5])

    def test_single_positive(self):
        self.assertEqual(rearrange([1]), [1])

    def test_single_negative(self):
        self.assertEqual(rearrange([-1]), [-1])

    def test_empty_list(self):
        self.assertEqual(rearrange([]), [])

    def test_zero_in_list(self):
        self.assertEqual(rearrange([0, -1, 2, -3, 4]), [-1, -3, 0, 2, 4])

    def test_large_numbers(self):
        self.assertEqual(rearrange(
            [1000000, -1000000, 500000, -500000]), [-1000000, -500000, 1000000, 500000])

    def test_duplicates(self):
        self.assertEqual(rearrange([1, -1, 1, -1]), [-1, -1, 1, 1])

    def test_already_sorted(self):
        self.assertEqual(
            rearrange([-3, -2, -1, 1, 2, 3]), [-3, -2, -1, 1, 2, 3])

    def test_reverse_sorted(self):
        self.assertEqual(
            rearrange([3, 2, 1, -1, -2, -3]), [-1, -2, -3, 3, 2, 1])


if __name__ == '__main__':
    main()
