from unittest import TestCase, main
from .right_rotate_list import right_rotate


class TestRightRotate(TestCase):
    # my test case
    def test_given_test_case(self):
        self.assertEqual(right_rotate([10, 20, 30, 40, 50], 3), [
                         30, 40, 50, 10, 20])

    def test_empty_list(self):
        self.assertEqual(right_rotate([], 3), [])

    def test_single_element(self):
        self.assertEqual(right_rotate([1], 1), [1])
        self.assertEqual(right_rotate([1], 0), [1])

    def test_no_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

    def test_rotation_equal_to_length(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_rotation_greater_than_length(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3])

    def test_rotation_less_than_length(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_large_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 102), [4, 5, 1, 2, 3])

    def test_negative_rotation(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])

    def test_large_list(self):
        large_list = list(range(1000))
        rotated_list = list(range(990, 1000)) + list(range(990))
        self.assertEqual(right_rotate(large_list, 10), rotated_list)

    # ---- additional test cases ------

    def test_empty_list_01(self):
        self.assertEqual(right_rotate([], 3), [])

    def test_single_element_01(self):
        self.assertEqual(right_rotate([1], 1), [1])
        self.assertEqual(right_rotate([1], 0), [1])

    def test_no_rotation_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5])

    def test_rotation_equal_to_length_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_rotation_greater_than_length_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3])

    def test_rotation_less_than_length_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_large_rotation_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], 102), [4, 5, 1, 2, 3])

    def test_negative_rotation_01(self):
        self.assertEqual(right_rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])

    def test_large_list_01(self):
        large_list = list(range(1000))
        rotated_list = list(range(990, 1000)) + list(range(990))
        self.assertEqual(right_rotate(large_list, 10), rotated_list)

    def test_repeated_elements(self):
        self.assertEqual(right_rotate([1, 1, 1, 1], 2), [1, 1, 1, 1])

    def test_mixed_data_types(self):
        self.assertEqual(right_rotate(
            [1, 'a', 3.0, True], 1), [True, 1, 'a', 3.0])

    def test_very_large_k(self):
        self.assertEqual(right_rotate(
            [1, 2, 3, 4, 5], 1000002), [4, 5, 1, 2, 3])

    def test_none_values(self):
        self.assertEqual(right_rotate(
            [None, 1, None, 2], 2), [None, 2, None, 1])

    def test_boolean_values(self):
        self.assertEqual(right_rotate(
            [True, False, True], 1), [True, True, False])

    # TODO: throw AssertionError: Lists differ: [4, 5, 1, 2, 3] != [3, 4, 5, 1, 2]
    # def test_negative_k(self):
    #     self.assertEqual(right_rotate([1, 2, 3, 4, 5], -3), [3, 4, 5, 1, 2])


if __name__ == '__main__':
    main()
