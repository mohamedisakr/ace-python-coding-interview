from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        length = len(piles)
        n = length // 3
        piles.sort()
        max_coins = 0

        for i in range(n, length, 2):
            max_coins += piles[i]
        return max_coins
