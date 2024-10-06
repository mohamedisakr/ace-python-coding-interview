def find_first_unique(lst):
    n = len(lst)

    for i in range(n):
        j = 0
        while j < n:
            if i != j and lst[i] == lst[j]:
                break
            j += 1
        if j == n:
            return lst[i]
    return None
