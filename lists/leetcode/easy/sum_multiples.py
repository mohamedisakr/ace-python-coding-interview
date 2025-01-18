# 2652. Sum Multiples
# https://leetcode.com/problems/sum-multiples/description/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_of_multiples(val: int) -> int:
            m = n // val
            return val * m * (m + 1) // 2

        sum_3 = sum_of_multiples(3)
        sum_5 = sum_of_multiples(5)
        sum_7 = sum_of_multiples(7)
        sum_15 = sum_of_multiples(15)  # Multiples of both 3 and 5
        sum_21 = sum_of_multiples(21)  # Multiples of both 3 and 7
        sum_35 = sum_of_multiples(35)  # Multiples of both 5 and 7
        sum_105 = sum_of_multiples(105)  # Multiples of 3, 5, and 7

        return sum_3 + sum_5 + sum_7 - sum_15 - sum_21 - sum_35 + sum_105

        # sum_multi = 0
        # for num in range(1, n+1, 1):
        #     if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        #         sum_multi += num
        # return sum_multi
