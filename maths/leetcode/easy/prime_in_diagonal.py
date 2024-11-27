# 2614. Prime In Diagonal
# https://leetcode.com/problems/prime-in-diagonal/description/
from typing import List


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def isPrime(n: int) -> bool:
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes1 = [row[i] for i, row in enumerate(nums) if isPrime(row[i])]
        primes2 = [row[-i - 1]
                   for i, row in enumerate(nums) if isPrime(row[-i - 1])]

        return max(max(primes1) if primes1 else 0,
                   max(primes2) if primes2 else 0)


# class Solution:
#     def diagonalPrime(self, nums: list[list[int]]) -> int:
#         def sieve(max_num):
#             is_prime = [True] * (max_num + 1)
#             is_prime[0] = is_prime[1] = False
#             for start in range(2, int(max_num**0.5) + 1):
#                 if is_prime[start]:
#                     for multiple in range(start*start, max_num + 1, start):
#                         is_prime[multiple] = False
#             return is_prime

#         max_num = max(max(row) for row in nums)
#         is_prime = sieve(max_num)

#         max_prime = 0
#         n = len(nums)

#         for i in range(n):
#             if is_prime[nums[i][i]]:
#                 max_prime = max(max_prime, nums[i][i])
#             if is_prime[nums[i][n-i-1]]:
#                 max_prime = max(max_prime, nums[i][n-i-1])

#         return max_prime

# class Solution:
#     def diagonalPrime(self, nums: List[List[int]]) -> int:
#         def isPrime(n: int) -> bool:
#             if n <= 1:
#                 return False
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     return False
#             return True

#         prime_1 = [row[i] for i, row in enumerate(nums) if isPrime(row[i])]
#         prime_2 = [row[-i - 1]
#                    for i, row in enumerate(nums) if isPrime(row[-i - 1])]

#         first = max(prime_1) if prime_1 else 0
#         second = max(prime_2) if prime_2 else 0

#         return max(first, second)

# # primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
# max_prime = 0
# m = len(nums)

# for i in range(m):
#     n = len(nums[i])
#     for j in range(n):
#         if i == j or i == n-i-1:
#             if isPrime(nums[i][j]):
#                 max_prime = max(max_prime, nums[i][j])

# return max_prime
