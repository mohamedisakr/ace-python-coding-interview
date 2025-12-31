def calculate_gp_sum_formula(n, a, r):
    """
    Core mathematical formula for the sum of a GP.
    """
    if r == 1:
        return a * n
    return a * (r**n - 1) / (r - 1)


def sum_nth_terms_less_one(n, a, r):
    return a * (1 - (r ** n)) / (1 - r)


def find_sum_nth_term(series, n):
    """
    Calculates the sum of n-th term of a GP based on a provided list.
    """
    if len(series) < 2:
        return "The series needs at least two numbers to determine the ratio."

    a = series[0]
    r = series[1] / a

    if -1 < abs(r) < 1:
        return sum_nth_terms_less_one(n, a, r)

    return calculate_gp_sum_formula(n, a, r)


my_series = [0.25, 0.75, 2.25, 6.75]
N = 7

result = find_sum_nth_term(my_series, N)

print(f"For the series {my_series}, the {N}th term is: {result}")
