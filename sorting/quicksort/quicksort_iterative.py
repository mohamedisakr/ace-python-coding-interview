from random import randint
from typing import List


def quicksort_iterative(arr: List[int]) -> None:
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))


def randomized_partition(arr: List[int], low: int, high: int) -> int:
    rand_index = randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]  # swap pivot to end
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
