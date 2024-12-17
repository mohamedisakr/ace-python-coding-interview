# 1792. Maximum Average Pass Ratio
# https://leetcode.com/problems/maximum-average-pass-ratio/description/

from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        old_pass_ratio = []
        for row in classes:
            division = row[0] / row[1]
            old_pass_ratio.append(division)
        print(f'normal pass ratio: {old_pass_ratio}')
        fixed_average_pass_ratio = sum(old_pass_ratio) / n
        print(f"fixed average pass ratio: {fixed_average_pass_ratio}")

        new_pass_ratio = []
        for row in classes:
            division = (row[0] + extraStudents) / (row[1] + extraStudents)
            new_pass_ratio.append(division)
        print(new_pass_ratio)
        moving_average_pass_ratio = sum(new_pass_ratio) / n
        print(f"moving average pass ratio: {moving_average_pass_ratio}")


# classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
# extraStudents = 4
classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2
sol = Solution()
sol.maxAverageRatio(classes, extraStudents)

# Example 2D array
# array_2d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Loop through the 2D array by their indices
# for i in range(len(classes)):
#     for j in range(len(classes[i])):
#         print(f"Element at index [{i}][{j}] is {classes[i][j]}")


# Result list to store the divisions
