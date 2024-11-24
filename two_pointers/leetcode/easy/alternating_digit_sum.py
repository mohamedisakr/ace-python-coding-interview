# 2544. Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/description/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits_sum = 0
        sign = 1

        while n > 0:
            sign *= -1
            digits_sum += n % 10 * sign
            n //= 10

        return sign * digits_sum


# return sum((-1) ** i * int(x) for i, x in enumerate(str(n)))
