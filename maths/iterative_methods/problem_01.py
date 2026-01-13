# # In Problems 1 to 7, use Newton’s method to solve
# # the equations given to the accuracy stated.
# # x^2 − 2x − 13 = 0, correct to 3 decimal places.
#
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
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print(f"Found solution after {n} iterations.")
            return xn

        dfxn = df(xn)
        if dfxn == 0:
            print("Zero derivative. No solution found.")
            return None

        # Newton's formula: x_{n+1} = x_n - f(x_n) / f'(x_n)
        xn = xn - (fxn / dfxn)

    print("Exceeded maximum iterations. No solution found.")
    return None

# --- Application to your specific equation: x^2 - 2x - 13 = 0 ---


# --- Application to your specific equation: x^2 - 2x - 13 = 0 ---

# Define the function and its derivative
def f(x): return x**2 - 2*x - 13
def df(x): return 2*x - 2


# Solve for the positive root starting at x=5
root = newton_method(f, df, x0=5, tol=0.0005)
print(f"Root: {root:.3f}")


# def f(x):
#     return x**2 - 2*x - 13


# def f_prime(x):
#     return 2*x - 2  # 2*(x - 1)


# def newton(x):
#     return x - (f(x)/f_prime(x))


# print(newton(4))

# # for x in range(-10, 11):
# #     print(f"x: {x}, f(x) : {f(x)}")
