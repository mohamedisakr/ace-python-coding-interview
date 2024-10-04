def find_sum(lst, k):
    seen = {}
    for number in lst:
        complement = k - number
        if complement in seen:
            return [complement, number]
        seen[number] = True
    return None  # Return None if no pair is found
