# 1979. Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
from typing import List
# from math import gcd


class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def findGCD(self, nums: List[int]) -> int:
        lo, hi = float('inf'), float('-inf')
        for n in nums:
            lo = min(n, lo)
            hi = max(n, hi)
        return self.gcd(lo, hi)


sol = Solution()
# a = 8
# b = 12
# print(sol.gcd(a, b))

nums = [3, 3]  # [7, 5, 6, 8, 3]  # [2, 5, 6, 9, 10]
print(sol.findGCD(nums))

# class Solution:
#     def findGCD(self, nums: List[int]) -> int:
#         return gcd(min(nums), max(nums))
