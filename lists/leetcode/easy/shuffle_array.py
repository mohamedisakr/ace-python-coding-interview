# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/description
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled = []
        for x, y in zip(nums[:n], nums[n:]):
            shuffled.append(x)
            shuffled.append(y)
        return shuffled


# nums = [2, 5, 1, 3, 4, 7]
# n = 3
nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
# Output: [1,4,2,3,3,2,4,1]
sol = Solution()
print(sol.shuffle(nums, n))
# Output: [2,3,5,4,1,7]

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         for i in range(n):
#             nums.insert(2 * i + 1, nums.pop(n + i))
#         return nums

# i, j = 1, n  # i = 0 -> n, j = n -> 2n

# while i < n and j < 2*n:
#     nums[i], nums[j] = nums[j], nums[i]
#     i += 1
#     j += 1

# return nums
