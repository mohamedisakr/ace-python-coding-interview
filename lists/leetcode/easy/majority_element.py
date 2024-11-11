# 169. Majority Element
# https://leetcode.com/problems/majority-element/description
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major_num = None

        for num in nums:
            if count == 0:
                major_num = num
            count += (1 if num == major_num else -1)

        return major_num


sol = Solution()
majority1 = sol.majorityElement([3, 2, 3])
majority2 = sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
print(majority1)
print(majority2)


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         visited_nums = {}
#         n = len(nums)
#         major = n//2
#         for item in nums:
#             if item not in visited_nums:
#                 visited_nums[item] = 1
#             else:
#                 visited_nums[item] += 1
#         return [key for key, value in visited_nums.items() if value >= major][0]
