def max_min(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            result[i] = arr[right]
            right -= 1
        else:
            result[i] = arr[left]
            left += 1
    return result


'''
arr = [1, 2, 3, 4, 5]
res = max_min(arr)
print(arr)
print(res)

arr1 = [1, 2, 3, 4, 5, 6, 7]
res1 = max_min(arr1)
print(arr1)
print(res1)

'''
