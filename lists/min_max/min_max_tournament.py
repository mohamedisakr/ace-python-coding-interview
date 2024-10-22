# Tournament Method
def min_max_arr_tournamtent(arr, lo, hi):
    if not arr:
        raise ValueError('List is empty')

    # only 1 element in the array
    if lo == hi:
        return arr[lo], arr[hi]

    # 2 elments in the array
    if hi - lo == 1:
        return min(arr[lo], arr[hi]), max(arr[lo], arr[hi])

    # more than 2 elements in the array
    mi = (hi+lo) // 2
    min_1, max_1 = min_max_arr_tournamtent(arr, lo, mi)
    min_2, max_2 = min_max_arr_tournamtent(arr, mi+1, hi)

    return (min(min_1, min_2), max(max_1, max_2))
