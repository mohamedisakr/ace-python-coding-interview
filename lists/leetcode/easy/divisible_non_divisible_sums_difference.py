# 2894. Divisible and Non-divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Sum of the first n natural numbers
        total_sum = n * (n + 1) // 2

        # Count of multiples of m up to n
        count_multiples = n // m

        # Sum of multiples of m
        sum_divisible_by_m = m * (count_multiples * (count_multiples + 1) // 2)

        # Sum of numbers not divisible by m
        sum_non_divisible = total_sum - sum_divisible_by_m

        # Difference of sums
        return sum_non_divisible - sum_divisible_by_m


# class Solution:
#     def differenceOfSums(self, n: int, m: int) -> int:
#         num1 = 0
#         num2 = 0
#         for i in range(1, n+1, 1):
#             if i % m != 0:
#                 num1 += i
#             elif i % m == 0:
#                 num2 += i

#         return num1 - num2
