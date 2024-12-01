# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/description/
from functools import reduce
from operator import or_


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return reduce(or_, [x, y])
        return (x ^ y).bit_count()
