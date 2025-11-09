def is_prime(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(num ** 0.5) + 1
    for divisor in range(3, limit, 2):  # check only odd divisors
        if num % divisor == 0:
            return False
    return True


def sieve(limit: int) -> list[int]:
    # Use a Sieve for Bulk Prime Detection
    primes = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i in range(3, limit) if is_prime[i]]


def sum_primes(lo: int, hi: int) -> int:
    total = 0
    for num in range(lo, hi, 2):
        if is_prime(num):
            total += num
    return total
