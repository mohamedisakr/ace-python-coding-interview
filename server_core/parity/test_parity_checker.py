import pytest
from parity_checker import is_even


@pytest.mark.parametrize("input_value, expected_output", [
    (4, True),  # Even number
    (5, False),  # Odd number
    (0, True),  # Zero
    (-4, True),  # Negative even number
    (-5, False),  # Negative odd number
    (1000000000, True),  # Large even number
    (1000000001, False),  # Large odd number
    (42, True),  # Even number
    (53, False),  # Odd number
    (-400, True),  # Negative even number
    (-501, False),  # Negative odd number
    (1000000000, True),  # Large even number
    (1000000001, False),  # Large odd number
    (1, False),  # Smallest odd integer
    (2, True),  # Smallest even integer
    (-2, True),  # Largest negative even integer
    (-1, False)  # Largest negative odd integer
])
def test_is_even(input_value, expected_output):
    assert is_even(input_value) == expected_output
