from unittest import TestCase, main
from .prime_sum import is_prime, sum_primes


class TestPrimeTools(TestCase):
    def test_is_prime_basic(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(997))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-7))

    def test_sum_primes_range(self):
        self.assertEqual(sum_primes(3, 10), 15)  # 3 + 5 + 7
        self.assertEqual(sum_primes(3, 1000), 76125)


if __name__ == "__main__":
    main()
