"""
https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


# sol = Solution
