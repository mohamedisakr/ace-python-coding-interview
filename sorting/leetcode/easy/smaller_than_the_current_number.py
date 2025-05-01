from collections import Counter
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_range = 100
        counter = Counter(nums)

        for i in range(1, max_range + 1):
            counter[i] += counter[i - 1]

        return [0 if num == 0 else counter[num - 1] for num in nums]


nums = [8, 1, 2, 2, 3]
# Output: [4,0,1,1,3]
sol = Solution()
print(sol.smallerNumbersThanCurrent(nums))
