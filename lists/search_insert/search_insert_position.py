"""
https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array&favoriteSlug=&difficulty=EASY
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid+1


sol = Solution
