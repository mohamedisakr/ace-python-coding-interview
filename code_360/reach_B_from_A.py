from math import gcd


def reachBFromA(a: int, b: int) -> int:
    if gcd(a, b) != 1:
        return 1
    return 0
