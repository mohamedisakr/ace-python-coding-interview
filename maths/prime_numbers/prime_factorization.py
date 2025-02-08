from typing import List
from sieve import sieve_to_numbers


def prime_factors(n: int) -> List[int]:
    sq_root = int((n**0.5) + 1)
    primes = []

    while n % 2 == 0 and n != 0:
        primes.append(2)
        n //= 2

    for divisor in range(3, sq_root, 2):
        while n % divisor == 0 and n != 0:
            primes.append(divisor)
            n //= divisor

    if n > 1:
        primes.append(n)

    return primes


# ex 01. Find the prime factorisation of the following numbers:
# numbers = [120, 200, 172, 138, 155, 235]

# for num in numbers:
#     print(f'{num} factors: {prime_factors(num)}')


# ex 02. Write 846 as a product of primes.
# num = 846
# print(f'{num} factors: {prime_factors(num)}')

# ex 03. Prove that a prime number can only give remainder 1 or 5 when divided by 6.
primes = sieve_to_numbers(100)
for num in primes:
    print(f'{num} % 6 = {num % 6}')
