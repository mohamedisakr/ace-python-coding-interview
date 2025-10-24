# numerical_methods.py

def newton_sqrt(k: float, epsilon: float = 1e-10, max_iter: int = 1000) -> float | None:
    """Compute square root using Newton-Raphson method."""
    if k < 0:
        return None
    if k == 0 or k == 1:
        return k

    guess = k / 2.0
    for _ in range(max_iter):
        square = guess * guess
        if abs(square - k) < epsilon:
            return guess
        guess -= (square - k) / (2 * guess)

    return guess


def newton_root(f, f_prime, x0: float, epsilon: float = 1e-10, max_iter: int = 1000) -> float | None:
    """Find root of f(x) using Newton-Raphson."""
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            return None
        x_new = x - fx / fpx
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x


def bisection(f, a: float, b: float, epsilon: float = 1e-10, max_iter: int = 1000) -> float | None:
    """Find root using bisection method."""
    if f(a) * f(b) > 0:
        return None
    for _ in range(max_iter):
        mid = (a + b) / 2
        fmid = f(mid)
        if abs(fmid) < epsilon or (b - a) / 2 < epsilon:
            return mid
        if f(a) * fmid < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2


def gradient_descent(f, grad_f, x0: float, learning_rate: float = 0.01, epsilon: float = 1e-6, max_iter: int = 1000) -> float:
    """Minimize f(x) using gradient descent."""
    x = x0
    for _ in range(max_iter):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x
