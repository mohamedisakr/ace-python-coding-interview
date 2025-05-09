from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        nums[:3] = sorted(nums[:3])
        return nums[1]
