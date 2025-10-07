# from .factorization import factor
from factorization import factor


def is_perfect_square_by_divisor_count(n: int) -> bool:
    """
    Returns True if n has an odd number of total divisors,
    which only happens if n is a perfect square.

    Time Complexity: O(sqrt(n)) — for prime factorization
    Space Complexity: O(1) — scalar counters only
    Auxiliary Space: O(1)

    Optimization Grade Insight:
        - Uses exponent counting to compute divisor count
        - Avoids building full factor lists
        - Ideal for number-theoretic checks and math-heavy pipelines
    """
    if n < 1:
        return False

    total_divisors = 1
    count = 0

    while n % 2 == 0:
        count += 1
        n //= 2

    if count > 0:
        total_divisors *= (count + 1)

    p = 3
    while p * p <= n:
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            total_divisors *= (count + 1)
        p += 2

    if n > 1:
        total_divisors *= 2  # n is prime

    return total_divisors % 2 == 1


# def is_perfect_square(num):
#     divs_set = set(factor(num))
#     length = len(divs_set)
#     return length % 2 == 1


# # num = 16
# nums = [5, 10, 15, 20, 25]
# for num in nums:
#     print(f'{num} : {is_perfect_square(num)}')

# # print(divs_set)
# # if length % 2 == 1:
# #     return True
# # else:
# #     return False
