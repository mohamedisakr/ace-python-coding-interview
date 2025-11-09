def is_prime(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer.")

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(num ** 0.5) + 1
    for divisor in range(3, limit, 2):  # check only odd divisors
        if num % divisor == 0:
            return False
    return True
