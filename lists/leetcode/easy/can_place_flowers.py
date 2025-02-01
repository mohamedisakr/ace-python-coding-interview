# Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/
from collections import Counter
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the previous and next plots are empty or if it's the boundary
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
