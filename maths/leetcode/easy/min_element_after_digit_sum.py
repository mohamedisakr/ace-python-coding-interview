# 3300. Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(map(int, str(num))) for num in nums)


nums = [999, 19, 199]
Output = 10

sol = Solution()
min_elem = sol.minElement(nums)
print(min_elem == Output)
# print("Minimum Element After Replacement With Digit Sum".lower())
# min_element = nums[0]
# for num in nums:
#     numerical = sum(int(digit) for digit in str(num))
#     min_element = min(numerical, min_element)
# return min_element
