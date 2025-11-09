def sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime
