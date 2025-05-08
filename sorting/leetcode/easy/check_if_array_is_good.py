from collections import Counter
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False

        counts = Counter(nums)

        # The largest number in a "good" array must be n - 1
        max_num = max(nums)
        if max_num != n - 1:
            return False

        # Check if n - 1 appears exactly twice
        if counts[n - 1] != 2:
            return False

        # Check if all other numbers from 1 to n - 2 appear exactly once
        for i in range(1, n - 1):
            if i != n - 1 and counts[i] != 1:
                return False

        # Check if there are any other numbers present
        if len(counts) != n - 1:
            return False

        return True


# class Solution:
#     def isGood(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n <= 1:
#             return False

#         counter = Counter(nums)

#         for i in range(1, n - 1):
#             if counter[i] != 1:
#                 return False

#         if counter[n-2] != 2:
#             return False

#         if len(counter) != n - 1:
#             return False

#         return True
