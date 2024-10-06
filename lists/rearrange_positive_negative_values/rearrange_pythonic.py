def rearrange(arr):
    return [item for item in arr if item < 0]+[item for item in arr if item >= 0]


'''
def rearrange(arr):
    n = len(arr)
    left = arr[0]
    rite = n-1

    while left < rite:
        # Move the left pointer to the right until a positive number is found
        while left < rite and arr[left] < 0:
            left += 1

        # Move the right pointer to the left until a negative number is found
        while left < rite and arr[rite] >= 0:
            rite -= 1

        # Swap the elements
        if left < rite:
            arr[left], arr[rite] = arr[rite], arr[left]

    return arr
'''
