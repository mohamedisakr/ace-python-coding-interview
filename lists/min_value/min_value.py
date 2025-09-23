from typing import List


def find_minimum(arr: List[int]) -> int:
    """
    Returns the minimum value in a non-empty list of integers.

    Args:
        arr (List[int]): List of integers.

    Returns:
        int: The smallest integer in the list.

    Raises:
        ValueError: If the input list is empty.
    """
    if not arr:
        raise ValueError("Input array must not be empty.")

    smallest = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


# arr = [9, 2, 3, 6]
# print(find_minimum(arr))
