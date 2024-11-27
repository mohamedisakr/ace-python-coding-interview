# 1037. Valid Boomerang
# https://leetcode.com/problems/valid-boomerang/description/

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        d_x = (x2 - x1)
        d_y = (y2 - y1)

        for point in points[2:]:
            x, y = point
            if (x - x1) * d_y == (y - y1) * d_x:
                return False

        return True
