from typing import List


def smallest_power_of_2(arr: List[int]) -> int:
    """
    Computes the smallest power of 2 that is greater than or equal to the sum of the input array.

    This function is useful in scenarios involving memory allocation, binary rounding, or 
    exponential scaling, where powers of 2 are preferred due to their alignment with binary systems.

    Parameters:
        arr (List[int]): A list of non-negative integers.

    Returns:
        int: The smallest power of 2 ≥ sum(arr).

    Time Complexity:
        O(n) — where n is the length of the array. The sum operation requires a single pass.

    Space Complexity:
        O(1) — no additional data structures are used beyond a few scalar variables.

    Auxiliary Space:
        O(1) — no recursion or dynamic memory allocation.

    Optimization Insight:
        - Uses bit-level rounding via `(x - 1).bit_length()` to compute ⌈log₂(x)⌉ efficiently.
        - Avoids floating-point operations (`math.log2`, `ceil`) for speed and precision.
        - Bit-shifting (`1 << k`) computes powers of 2 in constant time.
        - Ideal for systems-level tasks like buffer sizing, hash table growth, or binary tree depth estimation.

    Example:
        >>> smallest_power_of_2([1, 2, 3])
        8  # Because sum = 6, and 2^3 = 8 is the smallest power of 2 ≥ 6
    """
    total = sum(arr)
    return 1 << (total - 1).bit_length()
