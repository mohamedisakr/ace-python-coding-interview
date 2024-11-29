# 136. Single Number
# https://leetcode.com/problems/single-number/description/

from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
