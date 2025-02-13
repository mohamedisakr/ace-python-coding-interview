# 3232. Find if Digit Game Can Be Won
# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(num if num < 10 else -num for num in nums) != 0
