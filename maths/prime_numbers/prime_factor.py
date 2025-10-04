from typing import List


def factor(num: int) -> List[int]:
    primes = []
    while num % 2 == 0:
        primes.append(2)
        num //= 2

    for p in range(3, int(num ** 0.5)+1, 2):
        while num % p == 0:
            primes.append(p)
            num //= p

    if num > 1:
        primes.append(num)

    return primes


num = 6469693231  # 130
primes = factor(num)
print(primes)
