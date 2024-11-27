# 2413. Smallest Even Multiple
# https://leetcode.com/problems/smallest-even-multiple/description/
from math import lcm


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(n, 2)
