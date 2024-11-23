# 2180. Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

class Solution:
    def countEven(self, num: int) -> int:
        def sum_digits(num):
            return sum([int(digit) for digit in str(num)])

        return (num - sum_digits(num) % 2) // 2


# print("Count Integers With Even Digit Sum".lower())

# sol = Solution()
# evens = sol.countEven(30)
# print(evens)

# print((30 - 3 % 2) // 2)
# def is_even(num):
#     return sum_digits(num) % 2 == 0

# evens = 0
# # number = num-1
# for n in range(num, 0, -1):
#     print(n)
#     digits_sum = sum_digits(n)
#     if is_even(digits_sum):
#         evens += 1

# return evens
