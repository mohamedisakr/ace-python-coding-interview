# 263. Ugly Number
# https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
                if n == 1:
                    return True

        return n == 1
