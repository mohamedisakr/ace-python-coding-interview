# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
