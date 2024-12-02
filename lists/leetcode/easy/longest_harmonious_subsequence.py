# 594. Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/description/

from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        longest = 0
        for num in nums:
            if num+1 in counter:
                longest = max(longest, counter[num] + counter[num + 1])
        return longest
