def synthetic_division(coefficients, c):
    """
    Performs synthetic division of a polynomial by (x - c).
    :param coefficients: List of ints/floats (e.g., [1, -4, 0, 6] for x^3 - 4x^2 + 6)
    :param c: The root/value to divide by
    :return: (quotient coefficients, remainder)
    """
    # The first coefficient is always brought down as-is
    new_coeffs = [coefficients[0]]

    # Iterate through the remaining coefficients
    for i in range(1, len(coefficients)):
        # Multiply the previous result by 'c' and add the current coefficient
        next_val = (new_coeffs[-1] * c) + coefficients[i]
        new_coeffs.append(next_val)

    # The last value in the list is the remainder
    remainder = new_coeffs.pop()
    quotient = new_coeffs

    return quotient, remainder


# # Example: (2x^3 + 3x^2 - 8x + 3) / (x - 1)
# # Coefficients: [2, 3, -8, 3], c = 1
# coeffs = [2, 3, -8, 3]
# root = 1

# q, r = synthetic_division(coeffs, root)

# print(f"Quotient Coefficients: {q}")
# print(f"Remainder: {r}")


def my_synthetic_division(coeffs, root):
    n = len(coeffs)
    res_cofeffs = [coeffs[0]]
    for i in range(1, n):
        next_val = (res_cofeffs[-1] * root) + coeffs[i]
        res_cofeffs.append(next_val)
    remainder = res_cofeffs.pop()
    return res_cofeffs, remainder


# Example: (2x^3 + 3x^2 - 8x + 3) / (x - 1)
# Coefficients: [2, 3, -8, 3], c = 1
coeffs = [2, 3, -8, 3]  # will return [2, 5, -3]
root = 1

q, r = my_synthetic_division(coeffs, root)

print(f"Quotient Coefficients: {q}")
print(f"Remainder: {r}")
