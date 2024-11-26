# 762. Prime Number of Set Bits in Binary Representation
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(i.bit_count() in primes for i in range(left, right+1))

# count_primes = 0
# for num in range(left, right+1, 1):
#     set_bits = (num.bit_count())
#     if set_bits in primes:
#         count_primes += 1
# return count_primes


sol = Solution()
count_primes = sol.countPrimeSetBits(6, 10)
print(count_primes)

count_primes_1 = sol.countPrimeSetBits(10, 15)
print(count_primes_1)
