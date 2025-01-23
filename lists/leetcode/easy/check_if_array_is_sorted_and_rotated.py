# 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        # return sum(nums[i - 1] > num for i, num in enumerate(nums)) <= 1

        n = len(nums)
        rotates = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotates += 1

                if rotates > 1:
                    return False

        return True

    def is_sorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def is_sorted_and_rotated(self, nums):
        n = len(nums)

        for i in range(n):
            rotated = nums[i:] + nums[:i]
            if self.is_sorted(rotated):
                return True

        return False


# Example usage:
nums = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.is_sorted_and_rotated(nums))  # Output: True
