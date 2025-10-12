from unittest import TestCase, main
from .binary_decimal import to_binary


class TestToBinary(TestCase):
    def test_zero(self):
        self.assertEqual(to_binary(0), '0')

    def test_one(self):
        self.assertEqual(to_binary(1), '1')

    def test_small_numbers(self):
        self.assertEqual(to_binary(2), '10')
        self.assertEqual(to_binary(3), '11')
        self.assertEqual(to_binary(4), '100')
        self.assertEqual(to_binary(5), '101')
        self.assertEqual(to_binary(10), '1010')

    def test_powers_of_two(self):
        self.assertEqual(to_binary(8), '1000')
        self.assertEqual(to_binary(16), '10000')
        self.assertEqual(to_binary(1024), '10000000000')

    def test_large_numbers(self):
        self.assertEqual(to_binary(2**20), '1' + '0'*20)
        self.assertEqual(to_binary(10**6), bin(10**6)[2:])
        self.assertEqual(to_binary(2**63 - 1), bin(2**63 - 1)
                         [2:])  # Max signed 64-bit int

    def test_comparison_with_builtin_bin(self):
        for n in [0, 1, 5, 255, 1024, 999999, 2**31 - 1]:
            self.assertEqual(to_binary(n), bin(n)[2:])

    # def test_negative_input(self):
    #     with self.assertRaises(ValueError):
    #         to_binary(-1)

# Optional: modify to_binary to raise ValueError for negatives
# if num < 0:
#     raise ValueError("Negative numbers not supported")


if __name__ == '__main__':
    main()
