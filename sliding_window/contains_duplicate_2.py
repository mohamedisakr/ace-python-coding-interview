# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List

""" Find 2 equal numbers in the array that are at most k apart from each other.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k > n:
            return False
        index_dict = {}

        for key, val in enumerate(nums):
            index_dict[val] = key

        # Input: nums = [1,2,3,1], k = 3
        # Output: true
        for val, key in index_dict.items():
            print(val, key)
            # first = 0
            # second = 0
            # if nums[i] in index_dict:
            #     first = nums[i]


sol = Solution()
nums = [1, 2, 3, 1]
k = 3
print(sol.containsNearbyDuplicate(nums, k))

# lo = 0

# for hi in range(1, n):
#     if nums[lo] == nums[hi] and abs(hi - lo) <= k:
#         return True

#     if hi >= k - 1:
#         lo += 1

# return False
