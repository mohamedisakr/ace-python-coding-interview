# 1447. Simplified Fractions
# https://leetcode.com/problems/simplified-fractions/description

from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        for denom in range(2, n + 1):
            for nom in range(1, denom):
                if gcd(nom, denom) == 1:
                    fractions.append(f'{nom}/{denom}')
        return fractions
