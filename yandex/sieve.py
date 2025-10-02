# *Find all prime numbers less than or equal to a given number N.

def half_sieve(num: int) -> list[int]:
    """
    Efficiently computes all prime numbers up to a given num using a space-optimized 
    variant of the Sieve of Eratosthenes that skips even numbers.

    Parameters:
        num (int): The upper bound (inclusive) for prime number generation.

    Returns:
        List[int]: A list of all prime numbers ≤ num.

    Time Complexity:
        O(n log log n) — where n = num.
        This is the classic bound for sieving algorithms due to harmonic series behavior 
        over prime multiples.

    Space Complexity:
        O(n/2) — only odd indices are stored, reducing memory usage by ~50%.

    Auxiliary Space:
        O(n/2) — includes the boolean array for odd-number primality and the output list of primes.

    Optimization Insight:
        - Skips even numbers after 2 to halve memory and iteration cost.
        - Starts marking from i² to avoid redundant composite marking.
        - Appends primes incrementally during sieving to avoid post-processing.
        - Ideal for large-scale prime generation with tight memory constraints.

    Example:
        >>> half_sieve(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    n = (num // 2) + 1
    is_prime = [True] * n
    is_prime[0] = False  # 1 is not prime

    primes = [2]  # Start with the only even prime

    for i in range(3, int(num**0.5) + 1, 2):
        if is_prime[i // 2]:
            for j in range(i * i, num + 1, 2 * i):
                is_prime[j // 2] = False

    for i in range(3, num + 1, 2):
        if is_prime[i // 2]:
            primes.append(i)

    return primes


num = 20
primes = half_sieve(num)
print(primes)


# def half_sieve(num):
#     n = (num // 2) + 1
#     is_prime = [True] * n
#     is_prime[0] = False  # 1 is not prime

#     primes = [2]  # Start with the only even prime

#     for i in range(3, int(num**0.5) + 1, 2):
#         if is_prime[i // 2]:
#             for j in range(i * i, num + 1, 2 * i):
#                 is_prime[j // 2] = False

#     for i in range(3, num + 1, 2):
#         if is_prime[i // 2]:
#             primes.append(i)

#     return primes
