def find_sum(lst, k):
    seen = {}
    for number in lst:
        complement = k - number
        if complement in seen:
            return [complement, number]
        seen[number] = True
    return None  # Return None if no pair is found


'''
def find_sum(lst, k):
    n = len(lst)
    sums = []
    for i in range(n):
        for j in range(n):
            if lst[i]+lst[j] == k:
                sums.append(lst[i])
                sums.append(lst[j])
                return sums
'''
