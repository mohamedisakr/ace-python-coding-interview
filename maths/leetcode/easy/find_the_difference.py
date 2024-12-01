# 389. Find the Difference
# https://leetcode.com/problems/find-the-difference/description/
from typing import List
from functools import reduce
from operator import xor


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_xor = chr(reduce(xor, map(ord, s), 0))
        t_xor = chr(reduce(xor, map(ord, t), 0))
        return chr(ord(s_xor) ^ ord(t_xor))
