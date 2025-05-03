from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        triplets = 0
        freq = Counter(nums)

        for num, count in sorted(freq.items()):
            suffix = n - prefix - count
            triplets += suffix * prefix * count
            prefix += count

        return triplets
