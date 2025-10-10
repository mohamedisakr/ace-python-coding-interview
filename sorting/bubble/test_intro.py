from unittest import TestCase, main
from .intro import sort


class TestBubbleSort(TestCase):
    def test_basic_sorting(self):
        self.assertEqual(sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_already_sorted(self):
        self.assertEqual(sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        self.assertEqual(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_empty_list(self):
        self.assertEqual(sort([]), [])

    def test_single_element(self):
        self.assertEqual(sort([42]), [42])

    def test_negative_numbers(self):
        self.assertEqual(sort([-3, -1, -2, -5]), [-5, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(sort([3, -1, 0, 2, -5]), [-5, -1, 0, 2, 3])


if __name__ == '__main__':
    main()
