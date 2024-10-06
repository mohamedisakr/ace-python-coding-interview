from unittest import TestCase, main
from .non_repeating_integer import find_first_unique


class TestFindFirstUnique(TestCase):

    def test_single_element(self):
        self.assertEqual(find_first_unique([1]), 1)

    def test_all_unique_elements(self):
        self.assertEqual(find_first_unique([1, 2, 3, 4]), 1)

    def test_no_unique_elements(self):
        self.assertIsNone(find_first_unique([1, 1, 2, 2, 3, 3]))

    def test_first_element_unique(self):
        self.assertEqual(find_first_unique([1, 2, 2, 3, 3]), 1)

    def test_last_element_unique(self):
        self.assertEqual(find_first_unique([2, 2, 3, 3, 1]), 1)

    def test_middle_element_unique(self):
        self.assertEqual(find_first_unique([2, 2, 1, 3, 3]), 1)

    def test_multiple_unique_elements(self):
        self.assertEqual(find_first_unique([2, 3, 2, 4, 3, 5]), 4)

    def test_empty_list(self):
        self.assertIsNone(find_first_unique([]))

    def test_large_list(self):
        large_list = [i for i in range(1000)] + [500]
        self.assertEqual(find_first_unique(large_list), 0)

    def test_non_integer_elements(self):
        self.assertEqual(find_first_unique(['a', 'b', 'a', 'c', 'b']), 'c')


if __name__ == '__main__':
    main()
