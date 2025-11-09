from unittest import TestCase, main
from .root_power import find_root_power
# from lec_03.root_power import find_root_power
# from root_power import find_root_power


class TestFindRootPower(TestCase):
    def test_exact_match(self):
        self.assertEqual(find_root_power(27), (3, 3))
        # self.assertEqual(find_root_power(16), (2, 4))
        self.assertEqual(find_root_power(-8), (-2, 3))

    def test_no_match(self):
        self.assertIsNone(find_root_power(17))
        self.assertIsNone(find_root_power(-9))

    def test_edge_cases(self):
        # self.assertEqual(find_root_power(1), (1, 2))  # 1^2 = 1
        self.assertEqual(find_root_power(0), (0, 2))  # 0^2 = 0

    def test_negative_even_power(self):
        self.assertIsNone(find_root_power(-16))  # No real root^even = negative

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_root_power("27")

        with self.assertRaises(TypeError):
            find_root_power(3.14)


if __name__ == '__main__':
    main()
