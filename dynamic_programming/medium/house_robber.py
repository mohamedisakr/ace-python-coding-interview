# 198. House Robber
# https://leetcode.com/problems/house-robber/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        no_prev = nums[0]  # prev2
        with_prev = max(nums[0], nums[1])  # prev1

        for i in range(2, n):
            cur = max(with_prev, nums[i] + no_prev)
            no_prev = with_prev
            with_prev = cur

        return with_prev


test_cases = [[1, 2, 3, 1], [2, 7, 9, 3, 1]]
sol = Solution()
for test_case in test_cases:
    print(sol.rob(test_case))
