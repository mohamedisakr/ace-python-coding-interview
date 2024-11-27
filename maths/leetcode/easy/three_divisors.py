# 1952. Three Divisors
# https://leetcode.com/problems/three-divisors/description/
import math


class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False

        root = math.isqrt(n)
        return (root**2 == n and
                all(root % i != 0
                    for i in range(2, math.isqrt(root) + 1)))

# class Solution:
#     def isThree(self, n: int) -> bool:
#         if n == 1:
#             return False

#         root = int(n**0.5)

#         return (root**2 == n and all(root % i != 0 for i in range(2, int(n**0.5)+1)))

# for i in range(2, root+1):
#     if n % i == 0:
#         divs += 1
#     if divs == 3:
#         return True

# return False
