# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n > 0:
            n //= 5
            zeros += n
        return zeros


sol = Solution()
n = 100
print(sol.trailingZeroes(n))

# def trailingZeroes(self, n: int) -> int:
#     zeros = 0
#     exp = 1
#     quotient = n // 5**exp
#     while quotient != 0:
#         zeros += quotient
#         exp += 1
#         quotient = n // 5**exp

#     return zeros
