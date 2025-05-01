from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coors = [point[0] for point in points]
        x_coors.sort()
        widest_gap = 0
        n = len(x_coors)

        for i in range(n - 1):
            gap = x_coors[i+1] - x_coors[i]
            widest_gap = max(widest_gap, gap)
        return widest_gap


# [[8, 7], [9, 9], [7, 4], [9, 7]]
points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
sol = Solution()
widest_gap = sol.maxWidthOfVerticalArea(points)
print(widest_gap)
