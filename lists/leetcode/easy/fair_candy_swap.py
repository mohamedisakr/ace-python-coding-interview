# 888. Fair Candy Swap
# https://leetcode.com/problems/fair-candy-swap/description/
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) >> 1
        bob_sizes_set = set(bobSizes)

        for box in aliceSizes:
            target = box - diff
            if target in bob_sizes_set:
                return [box, target]
