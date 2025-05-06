from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        remain = nums[1:]
        remain.sort()
        return first + remain[0] + remain[1]
