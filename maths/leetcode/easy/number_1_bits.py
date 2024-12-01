# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n:
            n &= (n-1)
            set_bits += 1
        return set_bits
