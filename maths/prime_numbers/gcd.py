def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


cases = [
    [35, 12],
    [122, 39],
    [63, 42],
    [320, 80],
    [462, 200]]

for a, b in cases:
    print(gcd(a, b))
