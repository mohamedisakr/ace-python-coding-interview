# Iiterative Method
def min_max_arr_iterative(arr):
    if not arr:
        raise ValueError('List is empty')

    min_val = float('inf')
    max_val = float('-inf')

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return min_val, max_val
