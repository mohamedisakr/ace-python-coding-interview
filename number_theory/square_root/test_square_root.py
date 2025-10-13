from unittest import TestCase, main
from .square_root import sqr_root


class TestSqrRoot(TestCase):
    def test_perfect_squares(self):
        for n, expected in [(0, 0), (1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (100, 10), (1024, 32)]:
            self.assertEqual(sqr_root(n), expected)

    def test_non_perfect_squares(self):
        for n in [2, 3, 5, 10, 15, 26, 99, 101]:
            self.assertIsNone(sqr_root(n))

    def test_negative_numbers(self):
        for n in [-1, -4, -100]:
            self.assertIsNone(sqr_root(n))

    def test_large_perfect_square(self):
        self.assertEqual(sqr_root(2_147_395_600), 46340)  # 46340^2

    def test_large_non_perfect_square(self):
        self.assertIsNone(sqr_root(2_147_483_647))  # Max 32-bit signed int

    def test_boundary_cases(self):
        self.assertEqual(sqr_root(2**20), 2**10)
        self.assertIsNone(sqr_root(2**20 + 1))


if __name__ == '__main__':
    main()
