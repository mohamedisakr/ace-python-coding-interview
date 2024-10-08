def find_max_sum_sublist(arr):
    if not arr:
        return 0
    max_current = arr[0]
    max_global = arr[0]
    for item in arr[1:]:
        max_current = max(item, item + max_current)
        max_global = max(max_current, max_global)
    return max_global
