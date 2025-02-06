# Prefix Array: A prefix array ( or prefix sum array) is an array
# where each element at index i is the sum of the elements from
# the original array from the start to index i.
# This allows for quick calculation of the sum of any subarray.

# For example, let's say you have an array
# A = [1, 2, 3, 4, 5].
# The prefix array P would be
# [1, 3, 6, 10, 15].
# Here's how each element is computed:

# P[0] = A[0] = 1

# P[1] = P[0] + A[1] = 1 + 2 = 3

# P[2] = P[1] + A[2] = 3 + 3 = 6

# P[3] = P[2] + A[3] = 6 + 4 = 10

# P[4] = P[3] + A[4] = 10 + 5 = 15

from typing import List


class Solution:
    def prefix(self, nums: List[int]) -> List[int]:
        pass
