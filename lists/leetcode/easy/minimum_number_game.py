# 2974. Minimum Number Game
# https://leetcode.com/problems/minimum-number-game/description/
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums) - 1
        for i in range(0, n, 2):
            if i < n:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums


sol = Solution()
nums = [5, 4, 2, 3]
output = sol.numberGame(nums)
print(output)
