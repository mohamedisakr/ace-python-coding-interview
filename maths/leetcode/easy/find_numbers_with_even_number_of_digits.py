# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
from math import floor, log10
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for num in nums:
            try:
                log_10 = log10(num)
                digits = floor(log_10) + 1
                if digits % 2 == 0:  # has_even_digits(num) is True:
                    evens += 1
            except ValueError:  # Square root of a negative number.
                # raise ValueError(f'{num} must be positive integer')
                print(f'{num} must be positive integer')
        return evens
