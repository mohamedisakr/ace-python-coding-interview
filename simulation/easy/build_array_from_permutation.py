# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/description/

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i, num in enumerate(nums):
            nums[i] += n * (nums[num] % n)

        for i in range(n):
            nums[i] //= n

        return nums

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         return [nums[num] for num in nums]

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = n * 0
#         for i in range(n):
#             ans[i] = nums[nums[i]]
#         return ans
