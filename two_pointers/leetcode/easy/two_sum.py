# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], i]
            else:
                store[nums[i]] = i
        return [-1, -1]
