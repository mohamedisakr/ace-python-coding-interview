# 914. X of a Kind in a Deck of Cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
from typing import List
import math
import collections
import functools


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        return functools.reduce(math.gcd, count.values()) >= 2
