def find_max_sum_sublist(arr):
    if not arr:
        return 0
    max_current = arr[0]
    max_global = arr[0]
    for item in arr[1:]:
        max_current = max(item, item + max_current)
        max_global = max(max_current, max_global)
    return max_global


# Example usage:
array = [-2, -3, 4, -1, -2, 1, 5, -3]
print(find_max_sum_sublist(array))  # Output: 7

arr = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print(find_max_sum_sublist(arr))  # Output: 12
