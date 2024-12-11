# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if n < k:
            return 0.0

        current_sum = sum(nums[:k])
        max_sum = current_sum

        for hi in range(k, n):
            current_sum += nums[hi] - nums[hi - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k


# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))

# from typing import List


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         n = len(nums)
#         local_sum = 0
#         max_average = 0
#         lo = 0

#         for hi in range(n):
#             local_sum += nums[hi]

#             if hi == k-1:
#                 print(f'hi: {hi}')
#                 avg = local_sum / k
#                 max_average = max(avg, max_average)
#                 local_sum -= nums[lo]
#                 lo += 1

#         return max_average
