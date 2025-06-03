def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


cases = [
    [30, 96],
    [18, 24],
    [360, 48],
    [27, 39],
    [100, 63],
    [500, 300],
    [70, 42],
    [4, 9],
    [10, 27],
    [606060, 707070],
    [35, 12],
    [122, 39],
    [63, 42],
    [320, 80],
    [462, 200]]

for a, b in cases:
    print(f'{a} and {b}: {gcd(a, b)}')  # The GCD for # \t\t\t\t\t

# # (a) Use the Euclidean algorithm to show that 68 and 345 are relatively prime
# a, b = 68, 345
# print(f'{a} and {b} are relatively prime {is_coprime(a, b)}')
