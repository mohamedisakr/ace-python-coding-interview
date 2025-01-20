# 665. Non-decreasing Array
# https://leetcode.com/problems/non-decreasing-array/description/

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modifications = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                # Check if already more than one modification is needed
                if modifications == 1:
                    return False
                modifications += 1

                # Fix by modifying nums[i] or nums[i+1]
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]

        return True


# class Solution:
#     def checkPossibility(self, nums: List[int]) -> bool:
#         modifications = 0
#         n = len(nums) - 1
#         for i in range(n):
#             if nums[i] > nums[i+1]:
#                 if modifications == 1:
#                     return False
#                 modifications += 1
#         return True


nums = [4, 2, 1]
sol = Solution()
print(sol.checkPossibility(nums))
