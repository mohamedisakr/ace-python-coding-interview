# 1051. Height Checker
# https://leetcode.com/problems/height-checker/description/

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(actual != expt for actual, expt in zip(heights, expected))

# class Solution:
#     def heightChecker(self, heights: list[int]) -> int:
#         ans = 0
#         currentHeight = 1
#         count = [0] * 101

#         for height in heights:
#             count[height] += 1

#         for height in heights:
#             while count[currentHeight] == 0:
#                 currentHeight += 1
#             if height != currentHeight:
#                 ans += 1
#             count[currentHeight] -= 1

#         return ans
