# 2427. Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/description/

from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common_div = gcd(a, b)
        factors = 0
        for i in range(1, common_div+1):
            if a % i == 0 and b % i == 0:
                factors += 1
        return factors

# class Solution:
#     def commonFactors(self, a: int, b: int) -> int:
#         common_div = gcd(a, b)
#         return sum(a % i == 0 and b % i == 0 for i in range(1, common_div + 1))


# root_a = isqrt(a)
# root_b = isqrt(b)
# factors = 1

# for i in range(2, min(root_a, root_b)):
#     if a % i == 0 and b % i == 0:
#         factors += 1
# return factors
