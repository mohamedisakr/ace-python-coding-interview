from collections import Counter


def find_first_unique(lst):
    # Count the occurrences of each element in the list
    counts = Counter(lst)

    # Iterate through the list and return the first element with a count of 1
    for item in lst:
        if counts[item] == 1:
            return item
    return None  # In case there are no unique elements
