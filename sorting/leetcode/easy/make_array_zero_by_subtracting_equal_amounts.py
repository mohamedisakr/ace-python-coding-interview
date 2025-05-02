from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num})


nums = [1, 5, 0, 3, 5]
sol = Solution()
print(sol.minimumOperations(nums))
