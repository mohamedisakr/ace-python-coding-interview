from bisect import bisect_left
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        nums.sort()
        for index, value in enumerate(nums):
            insertion = bisect_left(nums, target - value, hi=index)
            pairs += insertion
        return pairs


nums = [-1, 1, 2, 3, 1]
target = 2
sol = Solution()
print(sol.countPairs(nums, target))
