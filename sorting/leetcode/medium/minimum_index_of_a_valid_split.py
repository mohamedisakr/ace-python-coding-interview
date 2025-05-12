from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        dominant, cnt = counter.most_common(1)[0]
        cur = 0
        for i, v in enumerate(nums, 1):
            if v == dominant:
                cur += 1
            if cur * 2 > i and ((cnt - cur) * 2) > n - i:
                return i - 1
        return -1


nums = [3, 3, 3, 3, 7, 2, 2]  # [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]  # [1, 2, 2, 2]
sol = Solution()
print(sol.minimumIndex(nums))
