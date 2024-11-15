# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/description/

from typing import List

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] % 2 == 0:
                lo += 1
            while lo < hi and nums[hi] % 2 != 0:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo+1, hi-1
        return nums

        # lo = 0
        # hi = len(nums) - 1

        # while lo < hi:
        #     if nums[lo] % 2 == 1 and nums[hi] % 2 == 0:
        #         nums[lo], nums[hi] = nums[hi], nums[lo]
        #     if nums[lo] % 2 == 0:
        #         lo += 1
        #     if nums[hi] % 2 == 1:
        #         hi -= 1

        # return nums
