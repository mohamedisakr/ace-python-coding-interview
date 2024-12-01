# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/description/

from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1 = -inf
        max_2 = -inf
        max_3 = -inf

        for num in nums:
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif max_1 > num and num > max_2:
                max_3 = max_2
                max_2 = num
            elif max_2 > num and num > max_3:
                max_3 = num

        return max_1 if max_3 == -inf else max_3
