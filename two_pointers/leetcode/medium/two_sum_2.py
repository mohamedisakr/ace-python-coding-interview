# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1

        while lo < hi:
            current_sum = numbers[lo]+numbers[hi]

            if current_sum == target:
                return [lo + 1, hi + 1]
            elif current_sum > target:
                hi -= 1
            else:
                lo += 1

        return []
