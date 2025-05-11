from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = [val for val in Counter(nums).values() if val > 1]
        return sum([(n * (n - 1)) // 2 for n in pairs])


nums = [1, 1, 1, 1]  # [1, 2, 3, 1, 1, 3]
sol = Solution()
print(sol.numIdenticalPairs(nums))

# print(pairs)
# counter = Counter(nums)


# freq = {}
# count = 0

# for num in nums:
#     if num in freq:
#         count += freq[num]
#     freq[num] = freq.get(num, 0) + 1

# return count
