from math import isqrt


def count_divisors(n: int) -> int:
    """
    Counts the number of positive divisors for a given integer n.
    This is a helper function.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    count = 0
    # Iterate from 1 up to the square root of n (inclusive)
    # We add 1 to int(math.sqrt(n)) to ensure the square root itself is included
    # if it's an integer.
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # If i*i == n, it means i is the square root (e.g., for n=9, i=3).
            # In this case, i and n/i are the same number, so we count it only once.
            if i * i == n:
                count += 1
            # Otherwise, i and n/i are distinct divisors (e.g., for n=6, (1,6) and (2,3)).
            # We count both.
            else:
                count += 2
    return count


def is_perfect_square_by_divisor_count(n: int) -> bool:
    """
    Determines if a positive integer is a perfect square by leveraging the
    mathematical fact that a number is a perfect square if and only if
    it has an odd number of divisors.

    Args:
        n: A positive integer.

    Returns:
        bool: True if the number is a perfect square, False otherwise.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    num_divisors = count_divisors(n)

    # Check if the total count of divisors is odd
    return num_divisors % 2 != 0


# --- Examples ---
# Define a list of numbers to test
test_numbers = [1, 4, 9, 16, 25, 100, 2, 6, 10, 12, 961, 999, 1000]


print("\n--- Testing is_perfect_square_by_divisor_count ---")
for num in test_numbers:
    try:
        result = is_perfect_square_by_divisor_count(num)
        # Determine expected output for clarity
        expected_div_count = count_divisors(num)
        expected = (expected_div_count % 2 != 0)
        print(
            f"Number {num}: Result = {result} (Divisors: {expected_div_count}, Expected = {expected}) {'[OK]' if result == expected else '[FAIL]'}")
    except ValueError as e:
        print(f"Number {num}: Error - {e}")

# print("--- Testing is_perfect_square_by_divisor_count (Perfect Square Check) ---")
# for num in test_numbers:
#     try:
#         result = is_perfect_square_by_divisor_count(num)
#         # Determine expected output for clarity
#         expected = (isqrt(num) * isqrt(num) == num)
#         print(
#             f"Number {num}: Result = {result} (Expected = {expected}) {'[OK]' if result == expected else '[FAIL]'}")
#     except ValueError as e:
#         print(f"Number {num}: Error - {e}")
