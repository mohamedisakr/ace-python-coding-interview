# 1232. Check If It Is a Straight Line
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        d_x = (x2 - x1)
        d_y = (y2 - y1)

        for point in coordinates[2:]:
            x, y = point
            if (x - x1) * d_y != (y - y1) * d_x:
                return False

        return True
