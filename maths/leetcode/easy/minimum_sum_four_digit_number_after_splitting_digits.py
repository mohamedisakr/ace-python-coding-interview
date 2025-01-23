# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        return int(s[0] + s[2]) + int(s[1] + s[3])


sol = Solution()
num = 4009  # 2931
print(sol.minimumSum(num))
# ---------------------------
# sol = Solution()
num = 2931
print(sol.minimumSum(num))

# ---------------------------

# def minimumSum(self, num: int) -> int:
#     digits = [int(digit) for digit in str(num)]
#     digits.sort()
#     num1 = digits[0] * 10 + digits[1]
#     num2 = digits[2] * 10 + digits[3]
#     return num1 + num2

# ---------------------------

# class Solution:
# def minimumSum(self, num: int) -> int:
#     # Convert the number to a list of its digits
#     digits = [int(digit) for digit in str(num)]

#     # Sort the digits
#     digits.sort()

#     # Form two new numbers and calculate their sum
#     # By combining the smallest two digits into one number
#     num1 = digits[0] * 10 + digits[2]
#     num2 = digits[1] * 10 + digits[3]

#     return num1 + num2
