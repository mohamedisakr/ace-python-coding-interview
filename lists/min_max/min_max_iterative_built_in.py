# built in min & max Method
def min_max_arr_built_in(arr):
    if not arr:
        raise ValueError('List is empty')

    min_val = min(arr)
    max_val = max(arr)

    return min_val, max_val
