def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


# cases = [
#     [35, 12],
#     [122, 39],
#     [63, 42],
#     [320, 80],
#     [462, 200]]

# for a, b in cases:
#     print(gcd(a, b))

# (a) Use the Euclidean algorithm to show that 68 and 345 are relatively prime
a, b = 68, 345
print(f'{a} and {b} are relatively prime {is_coprime(a, b)}')
