def merge_lists(lst1, lst2):
    m = len(lst1)
    n = len(lst2)

    if m == 0:
        return lst2
    if n == 0:
        return lst1

    # Ensure lst1 has enough space to accommodate elements from lst2
    lst1.extend([0] * n)

    # Start from the end of both lists
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if lst1[i] > lst2[j]:
            lst1[k] = lst1[i]
            i -= 1
        else:
            lst1[k] = lst2[j]
            j -= 1
        k -= 1

    # Copy remaining elements of lst2, if any
    while j >= 0:
        lst1[k] = lst2[j]
        j -= 1
        k -= 1

    return lst1
