# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/description/
import itertools
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        min_time = 0
        n = len(points)
        for i in range(1, n):
            min_time += max(abs(points[i][0] - points[i-1][0]),
                            abs(points[i][1] - points[i-1][1]))
        return min_time

# return sum(max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) for p1, p2 in itertools.pairwise(points))
