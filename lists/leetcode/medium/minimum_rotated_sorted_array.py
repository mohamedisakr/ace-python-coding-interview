# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        lo = 0
        hi = len(nums) - 1

        while hi > lo:
            mid = (hi+lo) // 2
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]
