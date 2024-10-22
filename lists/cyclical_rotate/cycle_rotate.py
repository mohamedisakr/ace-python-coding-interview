def cyclic_rotate(arr):
    n = len(arr)
    if n == 0:
        return arr

    last_item = arr[-1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last_item

    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
print(cyclic_rotate(arr))  # Output should be [5, 1, 2, 3, 4]
