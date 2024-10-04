def find_sum(lst, k):
    lst.sort()
    n = len(lst)
    first = 0
    last = n - 1
    total = 0

    while first != last:
        total = lst[first] + lst[last]
        if total == k:
            return [lst[first], lst[last]]
        elif total > k:
            last -= 1
        else:
            first += 1
    return None
