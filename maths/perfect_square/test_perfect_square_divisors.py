import unittest
from .perfect_square_divisors import is_perfect_square_by_divisor_count


class TestPerfectSquareByDivisorCount(unittest.TestCase):
    def test_basic_perfect_squares(self):
        for n in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
            self.assertTrue(is_perfect_square_by_divisor_count(
                n), f"{n} should be a perfect square")

    def test_non_perfect_squares(self):
        for n in [2, 3, 5, 6, 10, 15, 20, 50, 99]:
            self.assertFalse(is_perfect_square_by_divisor_count(
                n), f"{n} should not be a perfect square")

    def test_negative_numbers(self):
        for n in [-1, -4, -25, -100]:
            self.assertFalse(is_perfect_square_by_divisor_count(
                n), f"{n} should not be a perfect square")

    def test_edge_cases(self):
        self.assertFalse(is_perfect_square_by_divisor_count(0),
                         "0 should not be a perfect square")
        self.assertTrue(is_perfect_square_by_divisor_count(1),
                        "1 is a perfect square")

    def test_large_inputs(self):
        self.assertTrue(is_perfect_square_by_divisor_count(
            10**6), "1,000,000 is a perfect square")
        self.assertFalse(is_perfect_square_by_divisor_count(
            2_147_483_647), "Max 32-bit int should not be a perfect square")


if __name__ == '__main__':
    unittest.main()
