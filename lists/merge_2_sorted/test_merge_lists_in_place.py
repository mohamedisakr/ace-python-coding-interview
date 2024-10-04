# test_merge_lists.py
import unittest
from .merge_2_sorted_list_in_place import merge_lists


class TestMergeList(unittest.TestCase):

    def test_both_lists_empty(self):
        self.assertEqual(merge_lists([], []), [])

    def test_one_list_empty_1(self):
        self.assertEqual(merge_lists([1, 2, 3], []), [1, 2, 3])

    def test_one_list_empty_2(self):
        self.assertEqual(merge_lists([], [4, 5, 6]), [4, 5, 6])

    def test_both_lists_one_element_1(self):
        self.assertEqual(merge_lists([1], [2]), [1, 2])

    def test_both_lists_one_element_2(self):
        self.assertEqual(merge_lists([2], [1]), [1, 2])

    def test_multiple_elements_no_overlap(self):
        self.assertEqual(merge_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_multiple_elements_some_overlap(self):
        self.assertEqual(merge_lists([1, 3, 5], [3, 4, 6]), [1, 3, 3, 4, 5, 6])

    def test_duplicate_elements(self):
        self.assertEqual(merge_lists([1, 2, 2], [2, 3, 3]), [1, 2, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(merge_lists(
            [-3, -1, 2], [-2, 0, 3]), [-3, -2, -1, 0, 2, 3])

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(merge_lists(
            [-5, -3, 0, 2], [-4, -1, 1, 3]), [-5, -4, -3, -1, 0, 1, 2, 3])

    def test_all_elements_same(self):
        self.assertEqual(merge_lists([1, 1, 1], [1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_different_lengths_1(self):
        self.assertEqual(merge_lists([1, 3, 5, 7], [2, 4]), [1, 2, 3, 4, 5, 7])

    def test_different_lengths_2(self):
        self.assertEqual(merge_lists([1, 2], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    # ------- new test cases --------------
    def test_empty_lists(self):
        self.assertEqual(merge_lists([], []), [])

    def test_empty_lists_1(self):
        self.assertEqual(merge_lists([1, 2, 3], []), [1, 2, 3])

    def test_empty_lists_2(self):
        self.assertEqual(merge_lists([], [4, 5, 6]), [4, 5, 6])

    def test_single_element_lists(self):
        self.assertEqual(merge_lists([1], [2]), [1, 2])

    def test_single_element_lists_1(self):
        self.assertEqual(merge_lists([2], [1]), [1, 2])

    def test_already_sorted_lists(self):
        self.assertEqual(merge_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_already_sorted_lists_1(self):
        self.assertEqual(merge_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_lists_with_duplicates(self):
        self.assertEqual(merge_lists([1, 2, 2], [2, 3, 4]), [1, 2, 2, 2, 3, 4])

    def test_lists_with_duplicates_1(self):
        self.assertEqual(merge_lists([1, 1, 1], [1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_lists_with_negative_and_positive_numbers(self):
        self.assertEqual(merge_lists(
            [-3, -1, 2], [-2, 0, 3]), [-3, -2, -1, 0, 2, 3])

    def test_lists_with_negative_and_positive_numbers_1(self):
        self.assertEqual(merge_lists(
            [-5, -3, -1], [1, 3, 5]), [-5, -3, -1, 1, 3, 5])

    def test_large_lists(self):
        lst1 = list(range(0, 1000, 2))
        lst2 = list(range(1, 1000, 2))
        expected = list(range(1000))
        self.assertEqual(merge_lists(lst1, lst2), expected)

    # --------- edge test cases ----------
    def test_subset_lists(self):
        self.assertEqual(merge_lists([1, 2, 3], [2]), [1, 2, 2, 3])

    def test_subset_lists_1(self):
        self.assertEqual(merge_lists([2], [1, 2, 3]), [1, 2, 2, 3])

    def test_identical_elements(self):
        self.assertEqual(merge_lists([1, 1, 1], [1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_identical_elements_1(self):
        self.assertEqual(merge_lists([2, 2, 2], [2, 2, 2]), [2, 2, 2, 2, 2, 2])

    def test_different_lengths(self):
        self.assertEqual(merge_lists([1, 2], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_different_lengths_2(self):
        self.assertEqual(merge_lists([1, 2, 3, 4], [5]), [1, 2, 3, 4, 5])

    def test_extreme_values(self):
        self.assertEqual(merge_lists([float('-inf'), 0, float('inf')], [float('-inf'), 0, float('inf')]),
                         [float('-inf'), float('-inf'), 0, 0, float('inf'), float('inf')])

    def test_extreme_values_1(self):
        self.assertEqual(merge_lists(
            [float('-inf')], [float('inf')]), [float('-inf'), float('inf')])

    def test_floating_point_numbers(self):
        self.assertEqual(merge_lists([1.1, 2.2, 3.3], [1.1, 2.2, 3.3]), [
                         1.1, 1.1, 2.2, 2.2, 3.3, 3.3])

    def test_floating_point_numbers_1(self):
        self.assertEqual(merge_lists([1.5, 2.5], [1.0, 2.0, 3.0]), [
                         1.0, 1.5, 2.0, 2.5, 3.0])

    def test_non_numeric_elements_1(self):
        self.assertEqual(merge_lists(['apple'], ['banana', 'cherry']), [
                         'apple', 'banana', 'cherry'])

    # -------- additional edge cases ------

    def test_large_numbers(self):
        self.assertEqual(merge_lists(
            [10**10, 10**12], [10**11, 10**13]), [10**10, 10**11, 10**12, 10**13])

    def test_negative_numbers_only(self):
        self.assertEqual(merge_lists(
            [-5, -3, -1], [-4, -2, 0]), [-5, -4, -3, -2, -1, 0])

    def test_negative_and_positive_numbers(self):
        self.assertEqual(merge_lists(
            [3, 4, 5], [-2, -1, 0, 10]), [-2, -1, 0, 3, 4, 5, 10])

    def test_single_element_repeated(self):
        self.assertEqual(merge_lists([1, 1, 1], [1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_zeroes(self):
        self.assertEqual(merge_lists([0, 0, 0], [0, 0, 0]), [0, 0, 0, 0, 0, 0])

    def test_non_comparable_elements(self):
        with self.assertRaises(TypeError):
            merge_lists([1, 2, 3], ['a', 'b', 'c'])
    '''
    def test_non_numeric_elements(self):
        self.assertEqual(merge_lists(['a', 'c', 'e'], ['b', 'd', 'f']), [
                         'a', 'b', 'c', 'd', 'e', 'f'])
                         
    def test_repeated_patterns(self):
        self.assertEqual(merge_lists([1, 2, 1, 2], [3, 4, 3, 4]), [
                         1, 1, 2, 2, 3, 3, 4, 4])
                         
    def test_mixed_data_types(self):
        self.assertEqual(merge_lists([1, 'a', 3], [2, 'b', 4]), [
                         1, 2, 3, 'a', 'b', 4])
                         
    def test_null_values(self):
        self.assertEqual(merge_lists([None, 1, 2], [None, 3, 4]), [
                         None, None, 1, 2, 3, 4])
                         
    def test_special_characters(self):
        self.assertEqual(merge_lists(
            ['!', '@', '#'], ['$', '%', '^']), ['!', '$', '@', '%', '#', '^'])
    '''


if __name__ == '__main__':
    unittest.main()
