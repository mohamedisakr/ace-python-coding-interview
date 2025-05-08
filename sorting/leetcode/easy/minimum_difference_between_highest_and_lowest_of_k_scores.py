from math import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k > n or k <= 0:
            return 0

        nums.sort()
        min_diff = inf

        for i in range(n - k + 1):
            curr_diff = abs(nums[i] - nums[i + k - 1])
            min_diff = min(min_diff, curr_diff)

        return min_diff
