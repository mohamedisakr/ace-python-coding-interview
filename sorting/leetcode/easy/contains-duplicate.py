from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

            if num in counter and counter[num] > 1:
                return True

        return False


nums = [1, 2, 3, 1]
sol = Solution()
print(sol.containsDuplicate(nums))

# old solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         unique_cache = set()

#         for item in nums:
#             if item in unique_cache:
#                 return True
#             unique_cache.add(item)
#         return False
