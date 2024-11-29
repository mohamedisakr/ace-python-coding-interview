# 858. Mirror Reflection
# https://leetcode.com/problems/mirror-reflection/description/

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2

        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1


# class Solution:
#     def mirrorReflection(self, p: int, q: int) -> int:
#         com_div = gcd(p, q)

#         p_new = (p % com_div) // 2
#         q_new = (q % com_div) // 2

#         if p_new == 1 and q_new == 1:
#             return 1

#         return 0 if p_new == 1 else 2
