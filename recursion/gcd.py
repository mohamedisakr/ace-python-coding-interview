def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def gcd_iter(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


a = 9
b = 24
print(gcd(a, b))
