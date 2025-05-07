from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val, max_val = min(nums), max(nums)
        return sum(min_val < num < max_val for num in nums)


# [11, 7, 2, 15]  # -->  [2, 7, 11, 15]
nums = [-3, 3, 3, 90]
sol = Solution()
print(sol.countElements(nums))

# class Solution:
#     def countElements(self, nums: List[int]) -> int:
#         n = len(nums)
#         both = 0
#         nums.sort()
#         for i in range(1, n - 1, 1):
#             if nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
#                 both += 1
#         return both
