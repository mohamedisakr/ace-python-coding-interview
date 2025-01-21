# 674. Longest Continuous Increasing Subsequence
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        current_length = 1
        res = 1

        for i in range(1, n, 1):
            if nums[i] >= nums[i - 1]:
                current_length += 1
            else:
                current_length = 1
            res = max(res, current_length)

        return res
