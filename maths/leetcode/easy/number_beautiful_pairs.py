# 2748. Number of Beautiful Pairs
# https://leetcode.com/problems/number-of-beautiful-pairs/description/
from typing import List
from math import gcd


class Solution:
    def count_beautiful_pairs(self, nums: List[int]) -> int:
        leading_digits = [0] * 10
        beautiful_pairs = 0

        for number in nums:
            for digit in range(10):
                curr_digit = leading_digits[digit]
                if curr_digit and gcd(number % 10, digit) == 1:
                    beautiful_pairs += curr_digit

            leading_digits[int(str(number)[0])] += 1

        return beautiful_pairs


'''
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def firstDigit(num: int) -> int:
            return int(str(num)[0])

        def lastDigit(num: int) -> int:
            return num % 10

        n = len(nums)
        return sum(gcd(firstDigit(nums[i]), lastDigit(nums[j])) == 1
                   for i in range(n)
                   for j in range(i + 1, n))
'''

# n = len(nums)
# i = 0
# for j in range(n):
#     pass
