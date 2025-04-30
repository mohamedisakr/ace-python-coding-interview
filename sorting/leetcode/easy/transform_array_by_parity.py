

from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return ([0] * sum(num % 2 == 0 for num in nums) + [1] * sum(num % 2 == 1 for num in nums))


nums = [4, 3, 2, 1]
sol = Solution()
sorted_list = sol.transformArray(nums)
print(sorted_list)
