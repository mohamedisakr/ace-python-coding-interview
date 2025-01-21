# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -inf
        total = 0

        for num in nums:
            total = max(num, total + num)
            largest_sum = max(total, largest_sum)

        return largest_sum


# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         ans = -inf
#         summ = 0

#         for num in nums:
#             summ = max(num, summ + num)
#             ans = max(ans, summ)

#         return ans
