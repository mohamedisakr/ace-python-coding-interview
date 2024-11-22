# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n, l = len(nums), 1
        for r in range(1, n):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
