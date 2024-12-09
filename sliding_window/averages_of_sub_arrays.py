def find_averages_of_subarrays(arr, k):
    n = len(arr)
    averages = []
    lo = 0
    window_total = 0

    for hi in range(n):
        window_total += arr[hi]

        if hi >= k - 1:
            averages.append(window_total/k)
            window_total -= arr[lo]
            lo += 1

    return averages
