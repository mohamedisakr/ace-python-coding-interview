# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/description/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        a, b = a & MASK, b & MASK

        while b:
            carry = ((a & b) << 1) & MASK
            a, b = a ^ b, carry

        return a if a < 0x80000000 else ~(a ^ MASK)
