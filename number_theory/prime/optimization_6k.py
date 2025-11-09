def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

# for divisor in range(5, divisor * divisor <= n, 6)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
