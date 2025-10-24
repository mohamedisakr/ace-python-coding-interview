def newton_sqrt(k: float, epsilon: float = 1e-10, max_iter: int = 1000) -> float | None:
    """
    Computes the square root of k using Newton-Raphson method.
    Returns None if k is negative.

    Time Complexity: O(log log k) — quadratic convergence
    Space Complexity: O(1)
    Auxiliary Space: O(1)
    """
    if k < 0:
        return None
    if k in (0, 1):  # if k == 0 or k == 1:
        return k

    guess = k / 2.0
    for _ in range(max_iter):
        square = guess * guess
        if abs(square - k) < epsilon:
            return guess
        guess -= (square - k) / (2 * guess)

    return guess  # Return best approximation after max_iter

# def newton(k, epsilon):
#     guess = k / 2.0
#     rounds = 0

#     while abs(guess * guess - k) >= epsilon:
#         guess = guess - ((guess**2 - k)/(2 * guess))
#         rounds += 1

#     print(f'# of rounds = {rounds}')
#     return guess


# k = 24.0
# epsilon = 0.01
# guess = newton(k, epsilon)
# print(f'Square root of {k} is about {guess}')
