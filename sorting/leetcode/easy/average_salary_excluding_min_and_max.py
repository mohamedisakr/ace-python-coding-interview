from math import inf
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = inf
        max_val = -inf

        for num in salary:
            min_val = min(min_val, num)
            max_val = max(max_val, num)

        return (sum(salary) - min_val - max_val) / (len(salary) - 2)
