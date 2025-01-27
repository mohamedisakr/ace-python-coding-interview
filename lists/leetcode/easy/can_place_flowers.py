# Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/
from collections import Counter
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = Counter(flowerbed)
        return counter[0] >= 2*n + 1
