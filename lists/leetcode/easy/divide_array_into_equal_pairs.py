# 2206. Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/description/
from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for val in counter.values():
            if val % 2 != 0:
                return False
        return True
# return all(val % 2 == 0 for val in Counter(nums).values())
