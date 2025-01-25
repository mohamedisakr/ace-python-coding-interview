# 3289. The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, freq in counter.items() if freq > 1]
