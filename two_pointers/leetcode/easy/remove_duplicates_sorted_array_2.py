# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

from typing import List


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0

        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1

        return i


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         l, r = 0, 0

#         while r in range(n):
#             count = 1
#             while r + 1 < n and nums[r] == nums[r + 1]:
#                 r += 1
#                 count += 1

#             for i in range(min(2, count)):
#                 nums[l] = nums[r]
#                 l += 1
#             r += 1
#         return l
