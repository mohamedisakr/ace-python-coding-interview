from typing import List
from math import inf


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        min_1 = inf   # the minimum
        min_2 = inf   # the second minimum
        max_1 = -inf  # the maximum
        max_2 = -inf  # the second maximum
        max_3 = -inf  # the third maximum

        for num in nums:
            if num <= min_1:
                min_2 = min_1
                min_1 = num
            elif num <= min_2:
                min_2 = num

            if num >= max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num >= max_2:
                max_3 = max_2
                max_2 = num
            elif num >= max_3:
                max_3 = num

        return max(max_1 * min_1 * min_2, max_1 * max_2 * max_3)

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         large_3 = heapq.nlargest(3, nums)
#         small_2 = heapq.nlargest(2, nums, key=lambda x: -x)
#         large_3_prod = large_3[0]*large_3[1]*large_3[2]
#         small_2_prod = large_3[0]*small_2[0]*small_2[1]
#         return max(large_3_prod, small_2_prod)
