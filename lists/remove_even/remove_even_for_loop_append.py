def remove_even(lst):
    result = []
    for x in lst:
        if x % 2 != 0:
            result.append(x)
    return result
