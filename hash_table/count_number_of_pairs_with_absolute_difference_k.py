# 2006. Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
from collections import Counter
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs = 0
        counter = Counter()

        for num in nums:
            pairs += counter[num + k] + counter[num - k]
            counter[num] += 1

        return pairs

        # n = len(nums) - 1
        # for i in range(n):
        #     for j in range(n):
        #         if abs(nums[i] - nums[j] == k):
        #             pairs += 1
        # return pairs
