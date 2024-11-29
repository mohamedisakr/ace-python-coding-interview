# 866. Prime Palindrome
# https://leetcode.com/problems/prime-palindrome/description/


class Solution:
    def primePalindrome(self, n: int) -> int:
        def getPalindromes(n: int) -> int:
            length = n // 2
            for i in range(10**(length - 1), 10**length):
                s = str(i)
                for j in range(10):
                    yield int(s + str(j) + s[::-1])

        def isPrime(num: int) -> bool:
            return not any(num % i == 0 for i in range(2, int(num**0.5 + 1)))

        if n <= 2:
            return 2
        if n == 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        nLength = len(str(n))

        while True:
            for num in getPalindromes(nLength):
                if num >= n and isPrime(num):
                    return num
            nLength += 1

# class Solution:
#     def primePalindrome(self, n: int) -> int:
#         def is_prime(x):
#             if x < 2:
#                 return False
#             for i in range(2, int(x**0.5) + 1):
#                 if x % i == 0:
#                     return False
#             return True

#         def generate_palindromes():
#             for length in range(1, 6):  # Up to 5 digits will cover our needs
#                 # Odd-length palindromes
#                 for root in range(10**(length - 1), 10**length):
#                     s = str(root)
#                     yield int(s + s[-2::-1])  # e.g., 123 -> 12321
#                 # Even-length palindromes
#                 for root in range(10**(length - 1), 10**length):
#                     s = str(root)
#                     yield int(s + s[::-1])  # e.g., 123 -> 123321

#         if n <= 11:
#             for prime in [2, 3, 5, 7, 11]:
#                 if n <= prime:
#                     return prime

#         for palindrome in generate_palindromes():
#             if palindrome >= n and is_prime(palindrome):
#                 return palindrome

#         return -1  # In case something goes wrong, but practically this won't be hit


# class Solution:
#     def primePalindrome(self, n: int) -> int:
#         # Helper function to check if a number is prime.
#         def is_prime(x):
#             if x < 2:
#                 return False
#             divisor = 2
#             # Check divisors up to the square root of x.
#             while divisor * divisor <= x:
#                 if x % divisor == 0:
#                     return False
#                 divisor += 1
#             return True

#         # Helper function to reverse an integer number.
#         def reverse(x):
#             result = 0
#             while x:
#                 # Add the last digit of x to result.
#                 result = result * 10 + x % 10
#                 x //= 10  # Remove the last digit of x.
#             return result

#         # Loop until we find the palindrome prime.
#         while True:
#             # Check if the number is both a palindrome and prime.
#             if reverse(n) == n and is_prime(n):
#                 return n
#             # Skip all numbers between 10^7 and 10^8, as there are no 8-digit palindrome primes.
#             if 10**7 < n < 10**8:
#                 n = 10**8
#             n += 1  # Go to the next number.
