from random import randint
# Lomuto Partition Scheme (In-Place)


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot_index = randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # swap pivot to end
    pivot = arr[high]
    i = low  # boundary for elements < pivot
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
