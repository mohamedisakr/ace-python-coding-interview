from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        counter = Counter(nums1)

        for num in nums2:
            if counter[num] > 0:
                inter.append(num)
                counter[num] -= 1

        return inter

# old solution
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list((Counter(nums1) & Counter(nums2)).elements())
