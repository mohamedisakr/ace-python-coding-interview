from typing import List


def rearrange_in_place(arr: List[int]) -> None:
    """
    Rearranges the array in-place so that all negative values appear first,
    followed by positive values (including zero).

    Args:
        arr (List[int]): List of integers to rearrange.
    """
    j = 0  # boundary for negatives
    n = len(arr)
    for i in range(n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
