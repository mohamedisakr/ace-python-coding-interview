from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        while original in nums_set:
            original *= 2
        return original


nums = [5, 3, 6, 1, 12]
original = 3
# nums = [8, 19, 4, 2, 15, 3]
# original = 2
# Output: 4
my_solution = Solution()
print(my_solution.findFinalValue(nums, original))

# def findFinalValue(self, nums: List[int], original: int) -> int:
#     nums.sort()
#     for index, value in enumerate(nums):
#         if value == original:
#             original *= 2

#     return original
