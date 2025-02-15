# 3411. Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/

from functools import reduce
from math import gcd, lcm
from typing import List


class Solution:
    # def lcm(a, b):
    #     return a * b // gcd(a, b)

    def gcd_array(self, arr):
        return reduce(gcd, arr)

    def lcm_array(self, arr):
        return reduce(lcm, arr)

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                sub_arr = nums[i: j + 1]
                prod = reduce(lambda x, y: x * y, sub_arr, 1)
                gcd_val = self.gcd_array(sub_arr)
                lcm_val = self.lcm_array(sub_arr)
                if prod == gcd_val * lcm_val:
                    max_len = max(max_len, len(sub_arr))

        return max_len
