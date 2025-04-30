def isThereValidArray(n: int, s: int) -> int:
    numerator = 2 * s - (n * (n - 1))

    if numerator <= 0:
        return 0

    if numerator % (2 * n) != 0:
        return 0

    a0 = numerator // (2 * n)

    if a0 > 0:
        return 1

    return 0
