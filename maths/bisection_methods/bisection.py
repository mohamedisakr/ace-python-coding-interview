import math


def bisection_method_safe(func, a, b, tolerance=1e-6, max_iterations=100):
    # 1. Domain/Existence Check
    try:
        fa, fb = func(a), func(b)
    except (ValueError, ZeroDivisionError):
        return "Error: Function undefined at endpoints."

    # 2. IVT Sign Change Check
    if fa * fb >= 0:
        return "IVT Error: No sign change detected. Root not guaranteed."

    print(f"{'Iter':<10} {'Midpoint (c)':<20} {'f(c)':<20} {'Status'}")
    print("-" * 70)

    for i in range(1, max_iterations + 1):
        c = (a + b) / 2

        try:
            fc = func(c)
        except ZeroDivisionError:
            return f"Discontinuity found at x = {c}. Bisection failed."

        # 3. Continuity 'Heuristic' Check:
        # If f(c) is getting massive, we are likely hitting an asymptote (like 1/(x-2))
        if abs(fc) > 1e10:
            return f"Possible Asymptote detected near x = {c}. Stopping."

        print(f"{i:<10} {c:<20.6f} {fc:<20.6f} {'Searching...'}")

        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            return f"Success! Root found at: {c:.6f}"

        if func(a) * fc < 0:
            b = c
        else:
            a = c

    return f"Finished: Best approx is {c:.6f}"


# --- Testing the "Trap" function from Challenge 2 ---
# f(x) = 1 / (x - 2) between 1 and 3
def trap_func(x):
    return 1 / (x - 2)


print("Testing Discontinuous Function:")
print(bisection_method_safe(trap_func, 1, 3))

# Bouncing Root	(x−2)2	[1,3]	Touches 0 but doesn't cross it.'
def
# No Real Root	x2+4	[−1,1]	Function is always positive.
# Even No. of Roots	cos(x)	[0,2π]	Crosses twice, ending where it started.


# def bisection_method(func, a, b, tolerance=1e-6, max_iterations=100):
#     """
#     Finds a root of function 'func' in the interval [a, b]
#     using the Bisection Method.
#     """
#     # 1. Check the Intermediate Value Theorem condition
#     if func(a) * func(b) >= 0:
#         print("IVT Error: The function must have opposite signs at endpoints a and b.")
#         return None

#     print(f"{'Iter':<10} {'Midpoint (c)':<20} {'f(c)':<20}")
#     print("-" * 50)

#     for i in range(1, max_iterations + 1):
#         # 2. Find the midpoint
#         c = (a + b) / 2
#         f_c = func(c)

#         print(f"{i:<10} {c:<20.6f} {f_c:<20.6f}")

#         # 3. Check if we are close enough to the root (Tolerance)
#         if abs(f_c) < tolerance or (b - a) / 2 < tolerance:
#             return c

#         # 4. Decide which half to keep
#         if func(a) * f_c < 0:
#             b = c  # Root is in the left half [a, c]
#         else:
#             a = c  # Root is in the right half [c, b]

#     return c


# # --- Example Usage ---
# # Let's find the root of f(x) = x^3 - x - 1
# # We know from earlier it's between 1 and 2.
# # def my_function(x):
# #     return x**3 - x - 1


# # root = bisection_method(my_function, 1, 2)

# # if root:
# #     print("-" * 50)
# #     print(f"Final Approximate Root: {root:.6f}")

# # --- Continuity (Asymptote) Violation Example ---
# # Let's find the root of f(x) = x^3 - x - 1
# # We know from earlier it's between 1 and 2.


# def my_uncontinous_function(x):
#     return 1/x


# root = bisection_method(my_uncontinous_function, -1, 1)

# if root:
#     print("-" * 50)
#     print(f"Final Approximate Root: {root:.6f}")
