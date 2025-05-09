from math import inf

# loop through n digits - O(n)


class Solution:
    def maxProduct(self, n: int) -> int:
        first = -inf
        second = -inf

        while n > 0:
            digit = n % 10
            if digit > first:
                second = first
                first = digit
            elif digit > second:
                second = digit

            n = n // 10

        return first * second


n = 124
sol = Solution()
print(sol.maxProduct(n))

# sort O(nlogn)
# class Solution:
#     def maxProduct(self, n: int) -> int:
#         digits = list(map(int, str(n)))
#         digits.sort(reverse=True)
#         return int(digits[0]) * int(digits[1])
