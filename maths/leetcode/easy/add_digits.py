# 258. Add Digits
# https://leetcode.com/problems/add-digits/description/

class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1


sol = Solution()
num = 27
print(sol.addDigits(num))


# digits_sum = 0

# while num > 0:
#     digits_sum += num % 10
#     num //= 10

# one_digit_sum = 0

# while digits_sum > 10:
#     one_digit_sum += digits_sum % 10
#     digits_sum //= 10

# return one_digit_sum  # digits_sum
