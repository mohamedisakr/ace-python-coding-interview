# 492. Construct the Rectangle
# https://leetcode.com/problems/construct-the-rectangle/description/

from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)

        while area % width != 0:
            width -= 1

        return [area // width, width]


sol = Solution()
areas = [4, 37, 122122]
for area in areas:
    sol.constructRectangle(area)
