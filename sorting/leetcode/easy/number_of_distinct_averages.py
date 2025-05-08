from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 1

        nums.sort()

        averages = set()

        for i in range(n//2):
            avg = (nums[i] + nums[n - i - 1])
            averages.add(avg)

        return len(averages)

# old solution
# class Solution:
#     def distinctAverages(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 2:
#             return 1

#         nums.sort()

#         lo, hi = 0, n - 1
#         averages = set()

#         while lo < hi:
#             avg = (nums[lo] + nums[hi]) / 2
#             averages.add(avg)
#             lo += 1
#             hi -= 1

#         return len(averages)
