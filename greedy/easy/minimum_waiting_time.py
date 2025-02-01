# Problem: Minimum Waiting Time
# Goal: Schedule tasks to minimize the total waiting time for all tasks.

# Each task has a duration (e.g., [3, 2, 5]).

# The waiting time for a task is the sum of the durations of all tasks that started before it.

# Example:
# Tasks: [3, 2, 5]

# Optimal order: [2, 3, 5]

# Waiting time for 2: 0 (no tasks before it).

# Waiting time for 3: 2.

# Waiting time for 5: 2 + 3 = 5.

# Total waiting time: 0 + 2 + 5 = 7.
from typing import List


class Solution:
    def min_waiting_time(self, tasks: List[int]):
        tasks.sort()
        cumulative, total = 0, 0

        for duration in tasks[:-1]:
            cumulative += duration
            total += cumulative

        return total


tasks = [3, 2, 5]
sol = Solution()
print(sol.min_waiting_time(tasks))
