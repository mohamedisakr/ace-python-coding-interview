from typing import List


def right_rotate(arr: List[int], n: int) -> List[int]:
    """
    Rotates the array to the right by n positions.

    Args:
        arr (List[int]): List of elements to rotate.
        n (int): Number of positions to rotate.

    Returns:
        List[int]: Rotated array.
    """
    if not arr:
        return []
    n = n % len(arr)
    return arr[-n:] + arr[0:-n]


def right_rotate_in_place(arr: List[int], n: int) -> None:
    # to rotate in-place (e.g., for interview or memory-constrained environments),
    # you can use the reverse-rotate-reverse trick:
    n = n % len(arr)
    arr.reverse()
    arr[:n] = reversed(arr[:n])
    arr[n:] = reversed(arr[n:])


# arr = [1, 2, 3, 4, 5]
# n = 3
# print(right_rotate(arr, n))
