# 204. Count Primes
# https://leetcode.com/problems/count-primes/description/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        primes = [True] * n
        primes[0], primes[1] = False, False

        for i in range(4, n, 2):
            primes[i] = False

        for i in range(3, int(n ** 0.5) + 1, 2):
            if primes[i]:
                for j in range(i * i, n, i * 2):
                    primes[j] = False

        return sum(primes)
