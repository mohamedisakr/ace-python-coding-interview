def binary_search(arr, item):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            first = mid+1
        else:
            last = mid-1

    return -1


'''

def binary_search(arr, item):
    first = 0
    last = len(arr) - 1
    index = -1
    found = False

    while first <= last and not found:
        mid = (first + last)//2
        if arr[mid] == item:
            found = True
            index = mid
        else:
            if arr[mid] < item:
                last = mid-1
            else:
                first = mid+1

    if found:
        return index
    else:
        return -1
'''
