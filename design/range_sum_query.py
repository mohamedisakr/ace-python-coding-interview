# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

from typing import List
from itertools import accumulate


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# class NumArray:
#     def __init__(self, nums: List[int]):
#         n = len(nums)
#         # Adjusting to n+1 to avoid index issues
#         self.prefix_sum = [0] * (n + 1)
#         for i in range(n):
#             self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

#     def sumRange(self, left: int, right: int) -> int:
#         return self.prefix_sum[right + 1] - self.prefix_sum[left]


# class NumArray:
#     def __init__(self, nums: List[int]):
#         n = len(nums)
#         self.prefix_sum = [0] * n
#         self.prefix_sum[0] = nums[0]
#         for i in range(1, n):
#             self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]

#     def sumRange(self, left: int, right: int) -> int:
#         return self.prefix_sum[right] - self.prefix_sum[left]

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(left,right)


def prefix_sum_array(arr):
    prefix_sum = [0]
    for num in arr:
        print(f'num: {num}, prefix_sum[-1]: {prefix_sum[-1]
                                             }, num: {num} + prefix_sum[-1]: {num + prefix_sum[-1]}')
        prefix_sum.append(num + prefix_sum[-1])
    return prefix_sum


arr = [1, -20, -3, 30, 5, 4]
print(prefix_sum_array(arr))
