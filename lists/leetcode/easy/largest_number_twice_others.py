# 747. Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
from typing import List
from math import inf


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index = -1
        first, second = -inf, -inf

        for i, num in enumerate(nums):
            if num > first:
                second = first
                first = num
                index = i
            elif num > second:
                second = num

        return index if first >= 2*second else -1
