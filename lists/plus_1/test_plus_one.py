import pytest
from plus_one import Solution


@pytest.mark.parametrize("input_value, expected_output", [
    ([1, 2, 3], [1, 2, 4]),  # Simple Increment
    ([0], [1]),  # Single Digit Increment
    ([9, 9, 9], [1, 0, 0, 0]),  # All Digits as 9
    ([4, 3, 2, 1], [4, 3, 2, 2]),  # first example
    # ([0, 1, 2], [0, 1, 3]),  # Leading Zeros
    ([], [1]),  # Empty Input
    ([9], [1, 0]),  # Single Digit 9
    ([4, 9, 9], [5, 0, 0]),  # Mixed Digits with Carry
    ([1] * 1000, [1] * 999 + [2]),  # Large Number of Digits
])
def test_plusOne(input_value, expected_output):
    sol = Solution()
    assert sol.plusOne(input_value) == expected_output
