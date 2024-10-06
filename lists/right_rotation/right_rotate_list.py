def right_rotate(arr, k):
    if not arr or k == 0:
        return arr

    k = k % len(arr)  # Ensure k is within the bounds of the list length
    arr[:] = arr[-k:] + arr[:-k]  # In-place modification
    return arr
