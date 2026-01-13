# In Problems 1 to 7, use Newton’s method to solve
# the equations given to the accuracy stated.
# 3x^3 −10x = 14, correct to 4 significant figures.
def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    """
    Solves f(x) = 0 using Newton's method.

    :param f: The function to solve
    :param df: The derivative of the function
    :param x0: Initial guess
    :param tol: Tolerance (accuracy)
    :param max_iter: Maximum number of iterations
    :return: The root of the equation
    """
    xn = x0
    for i in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print(f"Found solution after {i} iterations.")
            return xn

        dfxn = df(xn)
        if dfxn == 0:
            print("Zero derivative. No solution found.")
            return None

        # Newton's formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
        xn = xn - (fxn / dfxn)

    print("Exceeded maximum iterations. No solution found.")
    return None

# --- Application to your specific equation: 3x^3 −10x = 14 ---

# Define the function and its derivative


def f(x): return (3*x**3 - 10*x - 14)
def df(x): return (9*x**2 - 10)


# Solve for the positive root starting at x=5
root = newton_method(f, df, x0=5, tol=0.0005)
print(f"Root: {root:.3f}")
