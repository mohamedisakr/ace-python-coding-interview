# 2798. Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        over_target = 0
        for hour in hours:
            if hour >= target:
                over_target += 1
        return over_target
