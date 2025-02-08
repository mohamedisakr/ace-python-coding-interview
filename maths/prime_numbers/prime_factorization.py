from typing import List
from math import sqrt, ceil


def extract_twos(n: int) -> List[int]:
    twos = []

    while n % 2 == 0 and n != 0:
        twos.append(2)
        n //= 2

    return twos


def prime_factors(n: int) -> List[int]:
    sq_root = (ceil(sqrt(n)))
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
num = 846
print(f'{num} factors: {prime_factors(num)}')
