def is_perfect_square(num: int) -> bool:
    """
    Determines whether a given non-negative integer is a perfect square.

    Parameters:
        num (int): The number to check.

    Returns:
        bool: True if num is a perfect square, False otherwise.

    Time Complexity:
        O(log n) — binary search over integer range.
    Space Complexity:
        O(1) — no extra data structures.
    Auxiliary Space:
        O(1) — scalar variables only.

    Optimization Grade Insight:
        - Uses integer-only binary search for precision and speed.
        - Avoids floating-point rounding errors.
        - Ideal for large-scale numeric validation or math-heavy pipelines.
    """
    if num < 0:
        return False

    if num == 0 or num == 1:
        return True

    lo, hi = 1, num

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        square = mid * mid

        if square == num:
            return True
        elif square < num:
            lo = mid + 1
        else:
            hi = mid - 1

    return False


'''
# nums = [1, 2, 3, 4, 5, 6, 7]
sqs = [1, 4, 9, 16, 25, 36, 49]

for num in sqs:
    print(f'{num}: {is_perfect_square(num)}')
'''
