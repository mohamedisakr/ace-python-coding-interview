from unittest import TestCase, main
from math import sqrt
from .newton import newton_sqrt


class TestNewtonSqrt(TestCase):
    def test_edge_cases(self):
        self.assertEqual(newton_sqrt(0), 0)
        self.assertEqual(newton_sqrt(1), 1)
        self.assertIsNone(newton_sqrt(-1))
        self.assertIsNone(newton_sqrt(-100))

    def test_perfect_squares(self):
        for k in [4, 9, 16, 25, 100, 1024]:
            result = newton_sqrt(k)
            self.assertAlmostEqual(result, sqrt(k), places=8)

    def test_non_perfect_squares(self):
        for k in [2, 3, 5, 10, 15, 99]:
            result = newton_sqrt(k)
            self.assertAlmostEqual(result, sqrt(k), places=8)

    def test_large_inputs(self):
        for k in [10**6, 2**31 - 1, 1e12]:
            result = newton_sqrt(k)
            self.assertAlmostEqual(result, sqrt(k), places=6)

    def test_custom_epsilon(self):
        self.assertAlmostEqual(newton_sqrt(
            2, epsilon=1e-2), sqrt(2), places=2)
        self.assertAlmostEqual(newton_sqrt(
            2, epsilon=1e-6), sqrt(2), places=6)


if __name__ == '__main__':
    main()
