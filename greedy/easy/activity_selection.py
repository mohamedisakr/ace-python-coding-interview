# Problem: Activity Selection
# Goal: Find the maximum number of non-overlapping activities you can perform,
#        given their start and end times.
# Rule: You can’t participate in two activities that overlap (the next activity
#        must start after the previous one ends).

# Example:
# Activities: [(1, 3), (2, 4), (3, 5)]

# Solution: You can do 2 activities (e.g., (1, 3) followed by (3, 5)).
# from math import inf
from typing import List


class Solution:
    def max_activities(self, activities: List[tuple[int]]):
        activities.sort(key=lambda arr: arr[1])
        non_overlap = 0
        last_end = -float("inf")

        for start, end in activities:
            if start >= last_end:
                non_overlap += 1
                last_end = end

        return non_overlap


sol = Solution()
activities = [(1, 3), (2, 4), (3, 5)]
print(sol.max_activities(activities))
