from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        count = Counter(digits)

        for first in range(1, 10):
            for middle in range(0, 10):
                for last in range(0, 9, 2):
                    if count[first] > 0 and count[middle] > (middle == first) and count[last] > (last == first) + (last == middle):
                        ans.append(first * 100 + middle * 10 + last)

        return ans
