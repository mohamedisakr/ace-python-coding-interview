# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/description/
from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(num for num, freq in counter.items() if freq == 1)


sol = Solution()
nums = [1, 1, 1, 1, 1]  # [1, 2, 3, 2]
print(sol.sumOfUnique(nums))
