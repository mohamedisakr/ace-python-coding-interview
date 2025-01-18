# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits, product_digits = 0, 1
        while n != 0:
            digit = n % 10
            sum_digits += digit
            product_digits *= digit
            n //= 10
        return product_digits - sum_digits


n = 234
sol = Solution()
print(sol.subtractProductAndSum(n))
