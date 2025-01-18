# 2535. Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num != 0:
                digit = num % 10
                digit_sum += digit
                num //= 10

        return abs(element_sum - digit_sum)


sol = Solution()
nums = [1, 15, 6, 3]
element_sum = sol.differenceOfSum(nums)
print(element_sum)
