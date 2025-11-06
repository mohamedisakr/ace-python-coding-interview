"""
tA: a tuple of numbers
tB: a tuple of numbers of the same length as tA
Assumes tA and tB are the same length.
Returns a tuple where the:
* first element is the length of one of the tuples
* second element is the sum of the pairwise products of tA and tB
"""


def dot_product(tA, tB):
    """
    Computes the dot product of two tuples of equal length.

    Parameters:
        tA (tuple[float]): First input tuple of numbers.
        tB (tuple[float]): Second input tuple of numbers, same length as tA.

    Returns:
        tuple[int, float]: A tuple where:
            - The first element is the length of the input tuples.
            - The second element is the dot product (sum of pairwise products).

    Time Complexity:
        O(n) — where n is the length of the tuples. Each element is visited once.

    Space Complexity:
        O(1) — no additional data structures are used.

    Auxiliary Space:
        O(1) — scalar accumulator only.

    Optimization Grade Insight:
        - Uses `zip()` for clean pairwise iteration.
        - Avoids intermediate lists or generators.
        - Ideal for numerical pipelines, vector math, or feature engineering.

    Example:
        >>> dot_product((1, 2, 3), (4, 5, 6))
        (3, 32)
    """
    prod = 0
    for a, b in zip(tA, tB):
        prod += a * b
    return (len(tA), prod)


# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB))  # prints (3,32)

tC = (7, 8, 9)
tD = (10, 11, 12)
print(dot_product(tC, tD))
