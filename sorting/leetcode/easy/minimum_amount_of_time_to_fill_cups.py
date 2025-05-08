from math import ceil
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        max_cup = max(amount)
        ceil_div = ceil(sum(amount) / 2)
        return max(max_cup, ceil_div)
