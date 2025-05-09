from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        missing = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                break
            missing += nums[i]

        while missing in num_set:
            missing += 1

        return missing

     #  algo monster
# def missingInteger(self, nums: List[int]) -> int:
#     nums.sort()  # Step 1: Sort the numbers in ascending order
#     missing = 1  # Step 2: Start tracking from 1 (smallest missing integer)

#     for num in nums:
#         if num >= missing:  # If current number can extend the sequence
#             missing += num
#         else:
#             return missing  # As soon as a gap is found, return the missing integer

#     return missing  # If no gap is found, return the next available integer


# --> gemini
# def missingInteger(self, nums: List[int]) -> int:
#     prefix_sum = 0
#     ans = 0
#     for num in nums:
#         prefix_sum += num
#         while ans <= prefix_sum:
#             ans += 1
#     return ans


# def missingInteger(self, nums: List[int]) -> int:
#     nums.sort()
#     prefix_sum = 0
#     for num in nums:
#         if num > prefix_sum + 1:
#             return prefix_sum + 1
#         prefix_sum += num
#     return prefix_sum + 1
