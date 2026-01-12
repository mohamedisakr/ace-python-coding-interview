from unittest import TestCase, main
from .quadratic_formula import quadratic_formula


class TestQuadraticFormula(TestCase):
    def assert_root_valid(self, a, b, c, root, tol=1e-9):
        """Helper: check that ax^2 + bx + c ≈ 0 for a given root."""
        val = a * (root**2) + b * root + c
        self.assertAlmostEqual(val, 0.0, delta=tol)

    def test_known_equation(self):
        # 5x^2 + 11x - 17 = 0
        roots = quadratic_formula(5, 11, -17)
        for r in roots:
            self.assert_root_valid(5, 11, -17, r)

    def test_perfect_square_discriminant(self):
        # x^2 - 2x + 1 = 0 → root = 1 (double root)
        roots = quadratic_formula(1, -2, 1)
        for r in roots:
            self.assert_root_valid(1, -2, 1, r)

    def test_complex_roots(self):
        # x^2 + 2x + 5 = 0 → roots are complex
        roots = quadratic_formula(1, 2, 5)
        for r in roots:
            self.assert_root_valid(1, 2, 5, r)

    def test_non_quadratic(self):
        # a = 0 should raise ValueError
        with self.assertRaises(ValueError):
            quadratic_formula(0, 2, 3)

    def test_random_small_range(self):
        # Sweep small coefficient ranges to benchmark correctness
        for a in range(1, 4):  # ensure a ≠ 0
            for b in range(-3, 4):
                for c in range(-3, 4):
                    roots = quadratic_formula(a, b, c)
                    for r in roots:
                        self.assert_root_valid(a, b, c, r)


if __name__ == "__main__":
    main()

# import unittest
# import sympy as sp
# from quadratic_formula import quadratic_formula  # your function


# class TestQuadraticFormula(unittest.TestCase):
#     def test_known_equation(self):
#         # Example: 5x^2 + 11x - 17 = 0
#         roots = quadratic_formula(5, 11, -17)
#         x = sp.symbols('x')
#         sympy_roots = sp.solve(5*x**2 + 11*x - 17, x)
#         # Compare numerical values
#         for r in roots:
#             self.assertTrue(any(abs(r - complex(sr.evalf()))
#                             < 1e-9 for sr in sympy_roots))

#     def test_random_equations(self):
#         x = sp.symbols('x')
#         for a in range(1, 6):  # keep 'a' small but nonzero
#             for b in range(-5, 6):
#                 for c in range(-5, 6):
#                     roots = quadratic_formula(a, b, c)
#                     sympy_roots = sp.solve(a*x**2 + b*x + c, x)
#                     # Ensure each root matches one of SymPy's roots
#                     for r in roots:
#                         self.assertTrue(
#                             any(abs(r - complex(sr.evalf())) < 1e-9 for sr in sympy_roots))

#     def test_non_quadratic(self):
#         # a = 0 should raise ValueError
#         with self.assertRaises(ValueError):
#             quadratic_formula(0, 2, 3)


# if __name__ == "__main__":
#     unittest.main()
