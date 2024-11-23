# 2553. Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/description/

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(digit) for num in nums for digit in str(num)]


# print("Separate the Digits in an Array".lower())
# sol = Solution()
# nums = [13, 25, 83, 77]
# answer = sol.separateDigits(nums)
# print(answer)
