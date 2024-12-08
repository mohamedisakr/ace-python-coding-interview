from sys import maxsize


def maxSubarraySum(arr, l):
    global_sum = -maxsize - 1  # maximum sum

    for i in range(l):
        for j in range(i, l):
            # subarray = arr[i.....j]
            local_sum = 0

            # add all the elements of subarray:
            for l in range(i, j+1):
                local_sum += arr[l]

            global_sum = max(global_sum, local_sum)

    return global_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    maxSum = maxSubarraySum(arr, n)
    print("The maximum subarray sum is:", maxSum)

# def compute(nums, k):
#     n = len(nums)
#     lo, hi = 0, k
#     total = 0

#     while hi < n-1:
#         for i in range(lo, hi):
#             total += nums[i]


# nums = [-1, 2, 3, 3, 4, 5, -1]
# k = 4
# print(compute(nums, k))

# lo, hi = 0, k
# total = 0

# for i in range(lo, hi, 1):
#     total += nums[i]

# return total
