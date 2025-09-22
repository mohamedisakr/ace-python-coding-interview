from typing import List


def find_sum_brute_force(arr: List[int], value: int) -> bool:
    """
    Returns True if any two distinct numbers in arr sum to 'value'.

    Args:
        arr (List[int]): List of integers.
        value (int): Target sum.

    Returns:
        bool: True if a valid pair exists, False otherwise.
    """
    for i, first in enumerate(arr):
        for j, second in enumerate(arr):
            if first + second == value and i != j:
                return True
    return False


def find_sum(arr: List[int], value: int) -> bool:
    seen = set()
    for num in arr:
        complement = value - num
        if complement in seen:
            return True
        seen.add(num)
    return False


arr = [1, 21, 3, 14, 5, 60, 7, 6]
value = 81
print(find_sum(arr, value))
