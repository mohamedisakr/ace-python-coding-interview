# 812. Largest Triangle Area
# https://leetcode.com/problems/largest-triangle-area/description/
from typing import List

# from itertools import combinations
import itertools


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(A, B, C):
            return 0.5 * abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

        def is_collinear(A, B, C):
            return A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]) == 0

        max_area = 0

        for A, B, C in itertools.combinations(points, 3):
            if not is_collinear(A, B, C):
                max_area = max(max_area, area(A, B, C))

        return max_area

# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         max_area = 0

#         for A_x, A_y in points:
#             for B_x, B_y in points:
#                 for C_x, C_y in points:
#                     max_area = max(max_area, 0.5 * abs((B_x - A_x) * (C_y - A_y) -
#                                                        (C_x - A_x) * (B_y - A_y)))
#         return max_area
