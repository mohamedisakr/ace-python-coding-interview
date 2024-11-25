from math import floor


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return floor(((2*n + 0.25) ** (0.5)) - 0.5)
