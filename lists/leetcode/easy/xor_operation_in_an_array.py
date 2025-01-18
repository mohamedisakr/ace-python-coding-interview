# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/description/

from functools import reduce
from operator import ixor


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        for i in range(n):
            nums[i] = start + 2 * i
        return reduce(ixor, nums)


sol = Solution()
print(sol.xorOperation(4, 3))
