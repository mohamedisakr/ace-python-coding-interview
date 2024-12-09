# 1. brute force
# 2. better solution
# 3. optimal

def brute_force(nums, k):
    ''' generate all sub-array    '''
    max_len = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total <= k:
                max_len = max(max_len, j-i+1)
            elif total > k:
                break

    return max_len


def better(nums, k):
    n = len(nums)
    lo, hi = 0, 0
    total, max_len = 0, 0

    while hi < n:
        total += nums[hi]

        while total > k:
            total -= nums[lo]
            lo += 1

            if total <= k:
                max_len = max(max_len, hi-lo+1)

        hi += 1

    return max_len


def optimal(nums, k):
    n = len(nums)
    lo, hi = 0, 0
    total, max_len = 0, 0

    while hi < n:
        total += nums[hi]

        if total > k:
            total -= nums[lo]
            lo += 1

            if total <= k:
                max_len = max(max_len, hi-lo+1)

        hi += 1

    return max_len
