# Problem: Job Sequencing with Deadlines
# Goal: Schedule jobs to maximize profit, given that each job has a deadline and a profit.

# Each job takes 1 unit of time to complete.

# You can only work on one job at a time.

# If a job is completed before or on its deadline, you earn its profit.

# Example:
# Jobs: [(1, 2, 100), (2, 1, 50), (3, 2, 200)]

# Format: (job_id, deadline, profit)

# Optimal schedule:

# Do job 3 at time 1 → profit = 200.

# Do job 1 at time 2 → profit = 100.

# Total profit: 300.

from typing import List


class Solution:
    def job_sequencing(self, jobs: List[int]) -> int:
        jobs.sort(key=lambda arr: -arr[2])
        # print(jobs)
        max_deadline = max(jobs, key=lambda arr: arr[1])[1]
        # print(f'max deadline: {max_deadline}')
        time_slots = [False] * (max_deadline + 1)
        total_profit = 0

        for _, deadline, profit in jobs:
            for slot in range(deadline, 0, -1):
                if not time_slots[slot]:
                    time_slots[slot] = True
                    total_profit += profit
                    break

        return total_profit


sol = Solution()
# Jobs = [(1, 2, 100), (2, 1, 50), (3, 2, 200)]
jobs = [
    ('J1',	5,	85),
    ('J2',	4,	25),
    ('J3',	3,	16),
    ('J4',	3,	40),
    ('J5',	4,	55),
    ('J6',	5,	19),
    ('J7',	2,	92),
    ('J8',	3,	80),
    ('J9',	7,	15)
]
print(sol.job_sequencing(jobs))


# ------
# for job in jobs:
#     deadline = job[1]

#     for slot in range(deadline, 0, -1):
#         if not time_slots[slot]:
#             time_slots[slot] = True
#             total_profit += job[2]
#             break
