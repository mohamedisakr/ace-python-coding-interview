def merge_lists(lst1, lst2):
    m = len(lst1)
    n = len(lst2)

    if m == 0:
        return lst2
    if n == 0:
        return lst1

    arr = []

    i = 0
    j = 0

    while i < m and j < n:
        if lst1[i] < lst2[j]:
            arr.append(lst1[i])
            i += 1
        else:
            arr.append(lst2[j])
            j += 1

    while i < m:
        arr.append(lst1[i])
        i += 1

    while j < n:
        arr.append(lst2[j])
        j += 1

    return arr
