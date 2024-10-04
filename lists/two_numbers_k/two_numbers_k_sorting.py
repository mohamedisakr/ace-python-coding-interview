from .binary_search import binary_search


def find_sum(lst, k):
    lst.sort()
    n = len(lst)
    for i in range(n):
        index = binary_search(lst, k-lst[i])
        if index != -1 and index != i:
            return [lst[i], k-lst[i]]
    return None
