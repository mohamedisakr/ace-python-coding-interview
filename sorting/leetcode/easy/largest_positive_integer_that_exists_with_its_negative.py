from collections import Counter
from math import inf
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        found = set()

        for num in nums:
            if -num in found:
                ans = max(ans, abs(num))
            else:
                found.add(num)

        return ans

        # max_twin = -1 * 1000000
        # counter = Counter(nums)

        # for num in counter:
        #     if -num in counter:
        #         max_num = max(num, -num)
        #         max_twin = max(max_twin, max_num)

        # if max_twin != -1 * 1000000:
        #     return max_twin
        # else:
        #     return -1


nums = [-10, 8, 6, 7, -2, -3]
sol = Solution()
print(sol.findMaxK(nums))
