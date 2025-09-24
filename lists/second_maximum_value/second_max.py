from typing import List, Optional


def find_second_max(arr: List[int]) -> Optional[int]:
    """
    Returns the second largest unique integer in the array.

    Args:
        arr (List[int]): List of integers with at least two unique values.

    Returns:
        int: Second largest unique integer.

    Raises:
        ValueError: If array has fewer than two unique values.
    """
    if len(set(arr)) < 2:
        raise ValueError("Array must contain at least two unique values.")

    first, second = float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second


# arr = [9, 2, 3, 6]
# # arr = [6, 9, 2, 3]
# print(find_second_max(arr))

# if arr[0] > arr[1]:
#     first = arr[0]
#     second = arr[1]
# else:
#     first = arr[1]
#     second = arr[0]
