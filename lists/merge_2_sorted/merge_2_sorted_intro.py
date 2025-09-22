from typing import List


def merge_lists(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merges two sorted integer arrays into a single sorted array.

    Args:
        arr1 (List[int]): First sorted array.
        arr2 (List[int]): Second sorted array.

    Returns:
        List[int]: Merged sorted array containing all elements from arr1 and arr2.
    """
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    res = []  # [0]*(m*n)  #

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    res.extend(arr1[i:])
    # while i < m:
    #     res.append(arr1[i])
    #     i += 1

    res.extend(arr2[j:])
    # while j < n:
    #     res.append(arr2[j])
    #     j += 1

    return res


'''
# arr1 = [1, 3, 4, 5]
# arr2 = [2, 6, 7, 8]
# res = merge_lists(arr1, arr2)
# print(res)

# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# res = merge_lists(arr1, arr2)
# print(res)

arr1 = [2]
arr2 = [1]
res = merge_lists(arr1, arr2)
print(res)
'''
