# 3334. Find the Maximum Factor Score of Array
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/description/

from functools import reduce
from math import gcd, lcm
from typing import List


def calculate_factor_score(num):
    score = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            score += i
            if i != num // i:
                score += num // i
    return score


def max_factor_score(arr):
    n = len(arr)
    dp = [0] * n
    factor_scores = [calculate_factor_score(num) for num in arr]

    print(f"Initial Factor Scores: {factor_scores}")

    dp[0] = factor_scores[0]

    for i in range(1, n):
        max_score = 0
        for j in range(i):
            if arr[i] % arr[j] == 0:
                max_score = max(max_score, dp[j])
        dp[i] = max_score + factor_scores[i]
        print(
            f"dp[{i}] = {dp[i]}, max_score = {max_score}, factor_score = {factor_scores[i]}")

    print(f"Final dp array: {dp}")
    return max(dp)


# Example usage
arr = [2, 4, 8, 16]
print(f"Maximum factor score: {max_factor_score(arr)}")


# class Solution:
#     def calculate_factor_score(self, num: int) -> int:
#         score = 0
#         for div in range(1, int(num**0.5) + 1):
#             if num % div == 0:
#                 score += div
#                 if div != num // div:
#                     score += num // div
#         return score

#     def maxScore(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = self.calculate_factor_score(nums[0])

#         for i in range(1, n):
#             max_score = 0
#             for j in range(i):
#                 if nums[i] % nums[j] == 0:
#                     max_score = max(max_score, dp[j])
#             dp[i] = max_score + self.calculate_factor_score(nums[i])

#         return max(dp)


# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         # Helper function to calculate the number of divisors
#         def count_divisors(n):
#             count = 0
#             for i in range(1, int(n**0.5) + 1):
#                 if n % i == 0:
#                     count += 1
#                     if i != n // i:
#                         count += 1
#             return count

#         # Calculate the score for each number and return the maximum score
#         max_score = 0
#         for num in nums:
#             score = count_divisors(num)
#             max_score = max(max_score, score)

#         return max_score


# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         nums.sort()
#         max_score = 0

#         # Checking all pairs of numbers to maximize the score
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 gcd_val = gcd(nums[i], nums[j])
#                 lcm_val = lcm(nums[i], nums[j])
#                 max_score = max(max_score, gcd_val * lcm_val)

#         return max_score

# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         # n = len(nums)
#         # min_val = reduce(min, nums)
#         # max_val = reduce(max, nums)
#         gcd_val = reduce(gcd, nums)
#         lcm_val = reduce(lcm, nums)

#         return gcd_val * lcm_val

# if gcd(min_val, max_val) == 0:
