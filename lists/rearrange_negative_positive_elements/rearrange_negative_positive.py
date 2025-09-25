from typing import List


def rearrange(arr: List[int]) -> List[int]:
    """
    Rearranges the array so that all negative values appear first,
    followed by positive values (including zero).

    Args:
        arr (List[int]): List of integers.

    Returns:
        List[int]: Rearranged list.
    """
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]
    return negatives + positives
