def reverse(arr):
    if not arr:
        raise ValueError('List is empty')

    n = len(arr)
    temp = [0]*n

    for i in range(n):
        temp[i] = arr[n - i - 1]

    return temp
