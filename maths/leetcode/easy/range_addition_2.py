# 598. Range Addition II
# https://leetcode.com/problems/range-addition-ii/description/
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows = m
        cols = n

        for a, b in ops:
            rows = min(a, rows)
            cols = min(b, cols)

        return rows * cols
