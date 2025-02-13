# 2240. Number of Ways to Buy Pens and Pencils
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/description/

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        for pens in range(0, total//cost1 + 1):
            remaining = total - (pens * cost1)
            pencils = remaining // cost2
            ways += pencils + 1

        return ways
