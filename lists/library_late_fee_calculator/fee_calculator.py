# https://leetcode.com/problems/library-late-fee-calculator
from typing import List


def calulatePenalty(day: int) -> int:
    if day == 1:
        return 1
    elif day > 5:
        return day * 3
    else:
        return day * 2


def lateFee(days_late: List[int]) -> int:
    total = 0
    for day in days_late:
        total += calulatePenalty(day)
    return total


daysLate = [5, 1, 7]  # [1, 1]  #
total_penalty = lateFee(daysLate)
print(total_penalty)
