from unittest import TestCase, main
from .perfect_square import is_perfect_square


class TestPerfectSquare(TestCase):

    def test_is_perfect_square(self):
        # ✅ Basic perfect squares
        assert is_perfect_square(0) == True
        assert is_perfect_square(1) == True
        assert is_perfect_square(4) == True
        assert is_perfect_square(9) == True
        assert is_perfect_square(16) == True
        assert is_perfect_square(25) == True
        assert is_perfect_square(36) == True
        assert is_perfect_square(49) == True
        assert is_perfect_square(100) == True

        # ❌ Non-perfect squares
        assert is_perfect_square(2) == False
        assert is_perfect_square(3) == False
        assert is_perfect_square(5) == False
        assert is_perfect_square(10) == False
        assert is_perfect_square(99) == False

        # ❌ Negative numbers
        assert is_perfect_square(-1) == False
        assert is_perfect_square(-4) == False
        assert is_perfect_square(-100) == False

        # ✅ Large perfect square
        assert is_perfect_square(10**6) == True
        assert is_perfect_square(2_147_395_600) == True  # 46340^2

        # ❌ Large non-perfect square
        assert is_perfect_square(2_147_395_601) == False
        # Max 32-bit signed int
        assert is_perfect_square(2_147_483_647) == False

        print("All test cases passed.")


# ✅ Run the tests
if __name__ == '__main__':
    main()

# Run the test suite
# test_is_perfect_square()
