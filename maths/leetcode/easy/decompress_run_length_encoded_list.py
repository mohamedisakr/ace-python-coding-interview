# 1313. Decompress Run_Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/description/
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            decompressed.extend([val] * freq)
        return decompressed


nums = [1, 1, 2, 3]  # [1, 2, 3, 4]
Output: [1, 3, 3]
# Output: [2,4,4,4]
sol = Solution()
print(sol.decompressRLElist(nums))

# class Solution:
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         decompressed = []
#         n = len(nums)
#         for i in range(1, n, 2):
#             freq, val = nums[i - 1], nums[i]
#             arr = [val]*freq
#             decompressed += arr
#         return decompressed
