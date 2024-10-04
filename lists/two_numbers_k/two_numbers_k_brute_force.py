
def find_sum(lst, k):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i]+lst[j] == k and i is not j:
                return [lst[i], lst[j]]
