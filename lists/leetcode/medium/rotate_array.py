# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        print(nums)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """
        Helper function to reverse a portion of the array in place.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(sol.rotate(nums, k))
