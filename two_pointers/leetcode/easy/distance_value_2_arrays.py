# 1385. Find the Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

from bisect import bisect_left
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def is_valid(item: int):
            index = bisect_left(arr2, item - d)
            return index == len(arr2) or arr2[index] > item + d

        arr2.sort()

        return sum(is_valid(item) for item in arr1)


# print("Find the Distance Value Between Two Arrays".lower())

# class Solution:
#     def findTheDistanceValue(
#         self,
#         arr1: list[int],
#         arr2: list[int],
#         d: int,
#     ) -> int:
#         ans = 0

#         arr2.sort()

#         for a in arr1:
#             i = bisect.bisect_left(arr2, a)
#             if ((i == len(arr2) or arr2[i] - a > d) and
#                     (i == 0 or a - arr2[i - 1] > d)):
#                 ans += 1

#         return ans
