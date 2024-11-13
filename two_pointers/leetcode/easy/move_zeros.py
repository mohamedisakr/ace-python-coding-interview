# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zero = 0

        # Traverse the Array: Move through the array with the current pointer.
        # When a non-zero element is found, swap it with the element at last_non_zero_found_at
        # and increment last_non_zero_found_at.
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1

        print(nums)


sol = Solution()
sol.moveZeroes([0, 1, 0, 3, 12])
