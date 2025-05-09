from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum([(cost[i]) for i in range(len(cost)) if i % 3 != 2])
