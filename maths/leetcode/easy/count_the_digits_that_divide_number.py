# 2520. Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description
class Solution:
    def countDigits(self, num: int) -> int:
        digits = 0
        n = num
        while num:
            d = num % 10
            if n % d == 0:
                digits += 1
            num //= 10
        return digits


sol = Solution()
digits = sol.countDigits(7)
print(digits)
