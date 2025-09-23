from collections import OrderedDict
from typing import List, Optional


def ordered_counter(iterable):
    counter = OrderedDict()
    for item in iterable:
        counter[item] = counter.get(item, 0) + 1
    return counter


def find_first_unique(arr: List[int]) -> Optional[int]:
    """
    Returns the first unique integer in the array using OrderedDict for order-preserving frequency count.

    Args:
        arr (List[int]): List of integers.

    Returns:
        Optional[int]: First unique integer, or None if none found.
    """
    freq = ordered_counter(arr)
    for num, count in freq.items():
        if count == 1:
            return num
    return None
