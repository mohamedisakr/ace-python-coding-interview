def find_minimum(arr):
    if not arr:
        raise ValueError("The array is empty")
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val


'''
arr1 = [9, 2, 3, 6]
print(find_minimum(arr1))

arr2 = [4, 2, 1, 5, 0]
print(find_minimum(arr2))
'''
