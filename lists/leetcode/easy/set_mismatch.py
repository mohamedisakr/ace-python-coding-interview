# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/description/
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = 0
        y = 0

        for i in range(1, n+1):
            x += nums[i-1] - i
            y += nums[i-1] ** 2 - i ** 2

        mis = (y - x**2) // (2 * x)
        dup = mis + x

        return [dup, mis]

# first solution using indices
# answer = [0, 0]

# for n in nums:
#     n = abs(n)
#     nums[n - 1] = -nums[n - 1]

#     if nums[n - 1] > 0:
#         answer[0] = n

# for i, n in enumerate(nums):
#     if n > 0 and i+1 != answer[0]:
#         answer[1] = i + 1
#         return answer

# first solution using hashmap
# answer = [0, 0]
# counter = Counter(nums)
# n = len(nums)

# for i in range(n + 1):
#     if counter[i] == 0:
#         answer[1] = i

#     if counter[i] == 2:
#         answer[0] = i

# return answer
