def find_second_maximum(lst):
    if len(lst) < 2:
        return None  # Not enough elements to find the second maximum

    max_val = float('-inf')
    second_max = float('-inf')

    for item in lst:
        if item > max_val:
            second_max = max_val
            max_val = item
        elif item > second_max and item != max_val:
            second_max = item

    if second_max != float('-inf'):
        return second_max
    else:
        return None
    # return second_max if second_max != float('-inf') else None


'''
def find_second_maximum(lst):
    max_val = lst[0]
    second_max = lst[0]

    for item in lst:
        if item > max_val:
            second_max = max_val
            max_val = item
    return second_max
'''
