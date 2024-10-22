def reverse_in_place(arr):
    if not arr:
        raise ValueError('List is empty')

    n = len(arr)

    for i in range(n):
        arr[i],  arr[n - i - 1] = arr[n - i - 1], arr[i]

    return arr
