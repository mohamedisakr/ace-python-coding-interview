from typing import List


primes_up_to_150 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                    61, 67, 71, 73, 79, 83,	89,	97, 101, 103, 107, 109, 113, 127,
                    131, 137, 139, 149]


def compute_divisors(num: int) -> List[int]:
    root = int(num**0.5) + 1
    # print(f'root: {root}')
    factors = []
    for _, p in enumerate(primes_up_to_150):
        if p < root:
            while num % p == 0:
                factors.append(p)
                num //= p

    if num > 1:
        factors.append(num)
    return factors


# num = 1673  # 2025  # 144  # 36  # 28  # 2005  #
# factors = compute_divisors(num)
# print(factors)

years = [1990, 1991, 1992, 1993, 1994]
for year in years:
    print(f'{year}: {compute_divisors(year % 100)}')
    # print(f'{year}: {compute_divisors(year)}')

# print(f'{years[0]} mod 100 = {years[0] % 100}')
