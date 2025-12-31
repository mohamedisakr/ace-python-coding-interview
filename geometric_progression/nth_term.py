def calculate_gp_nth_term(a, r, n):
    """Mathematical formula for the n-th term of a GP."""
    return a * (r ** (n - 1))


def find_nth_term_from_series(series, n):
    """
    Calculates the n-th term of a GP based on a provided list.
    """
    if len(series) < 2:
        return "The series needs at least two numbers to determine the ratio."

    a = series[0]
    r = series[1] / a
    return calculate_gp_nth_term(a, r, n)


my_series = [5, 10, 20, 40]
target_n = 10

result = find_nth_term_from_series(my_series, target_n)

print(f"For the series {my_series}, the {target_n}th term is: {result}")
