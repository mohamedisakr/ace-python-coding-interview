# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/description/


from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0
        while lo <= hi:
            if people[lo]+people[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats
