from math import inf
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        max_pair = -inf
        nums.sort()

        while lo < hi:
            sum_pair = nums[lo] + nums[hi]
            max_pair = max(max_pair, sum_pair)
            lo += 1
            hi -= 1

        return max_pair


nums = [3, 5, 4, 2, 4, 6]  # [3, 5, 2, 3]
sol = Solution()
print(sol.minPairSum(nums))
