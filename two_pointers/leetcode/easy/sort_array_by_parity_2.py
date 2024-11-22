# 922. Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1

        while i < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 != 0:
                j += 2
            if i < n:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
