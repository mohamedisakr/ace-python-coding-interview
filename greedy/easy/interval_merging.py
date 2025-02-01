# Problem: Merge Intervals
# Goal: Merge all overlapping intervals in a list and return the non-overlapping intervals in sorted order.

# Example:
# Input: [[1, 3], [2, 6], [8, 10], [15, 18]]

# Output: [[1, 6], [8, 10], [15, 18]]

# Explanation: [1, 3] and [2, 6] overlap → merged into [1, 6].


from typing import List


class Solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda arr: arr[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1]
            if start <= last[1]:  # overlap
                merged[-1] = [last[0], max(last[1], end)]
            else:
                merged.append([start, end])

        return merged


sol = Solution()
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
print(sol.merge_intervals(intervals))
