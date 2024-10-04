def merge_lists(lst1, lst2):
    m = len(lst1)
    n = len(lst2)

    if m == 0:
        return lst2
    if n == 0:
        return lst1

    arr = [0] * (m + n)

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if lst1[i] > lst2[j]:
            arr[k] = lst1[i]
            i -= 1
        else:
            arr[k] = lst2[j]
            j -= 1
        k -= 1

    while i >= 0:
        arr[k] = lst1[i]
        i -= 1
        k -= 1

    while j >= 0:
        arr[k] = lst2[j]
        j -= 1
        k -= 1

    return arr
