# sort Method
def min_max_arr_sort(arr):
    if not arr:
        raise ValueError('List is empty')
    arr.sort()
    return arr[0], arr[-1]
