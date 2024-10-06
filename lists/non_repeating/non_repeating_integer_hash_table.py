from collections import Counter


def find_first_unique(lst):
    stops = {}
    unique = {}
    for item in lst:
        if item not in stops and item not in unique:
            stops[item] = item
            unique[item] = item
        elif item in stops:
            if item in unique:
                del unique[item]

    # Retrieve the first key-value pair
    try:
        first_key, first_value = next(iter(unique.items()))
    except StopIteration:
        return None
    return first_value
