from cmath import sqrt  # handles complex numbers safely


def quadratic_formula(a: float, b: float, c: float):
    """
    Solve ax^2 + bx + c = 0 using the quadratic formula.
    Returns a tuple of two roots (real or complex).
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' must not be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c
    sqrt_disc = sqrt(discriminant)  # works for both real and complex

    root1 = (-b - sqrt_disc) / (2*a)
    root2 = (-b + sqrt_disc) / (2*a)

    return (root1, root2)
