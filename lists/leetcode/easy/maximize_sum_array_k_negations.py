# 1005. Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/

from collections import Counter
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # If k is odd, flip the smallest element
        if k % 2 == 1:
            nums.sort()  # Ensure the smallest element is at the start
            nums[0] = -nums[0]

        return sum(nums)

# class Solution:
#     def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
#         counter = Counter(nums)

#         for i in range(-100, 0):
#             if counter[i]:
#                 num_negations = min(counter[i], k)
#                 counter[i] -= num_negations
#                 counter[-i] += num_negations
#                 k -= num_negations
#                 if k == 0:
#                     break

#         if k % 2 == 1 and counter[0] == 0:
#             for i in range(1, 101):
#                 if counter[i]:
#                     counter[i] -= 1
#                     counter[-i] += 1
#                     break

#         return sum(key * value for key, value in counter.items())


# class Solution:
#     def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
#         nums.sort()

#         for i, num in enumerate(nums):
#             if num > 0 or k == 0:
#                 break
#             nums[i] = -num
#             k -= 1

#         return sum(nums) - (k % 2) * min(nums) * 2
