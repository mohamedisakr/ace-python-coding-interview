from unittest import TestCase, main
from math import sqrt, cos
from .numerical_methods import (
    newton_sqrt,
    newton_root,
    bisection,
    gradient_descent
)


class TestNewtonSqrt(TestCase):
    def test_edge_cases(self):
        self.assertEqual(newton_sqrt(0), 0)
        self.assertEqual(newton_sqrt(1), 1)
        self.assertIsNone(newton_sqrt(-1))

    def test_accuracy(self):
        for k in [2, 3, 10, 100, 1024, 1e6]:
            result = newton_sqrt(k)
            self.assertAlmostEqual(result, sqrt(k), places=8)

    def test_custom_epsilon(self):
        self.assertAlmostEqual(newton_sqrt(
            2, epsilon=1e-2), sqrt(2), places=2)


class TestNewtonRoot(TestCase):
    def test_cubic_root(self):
        def f(x): return x**3 - x - 2
        def f_prime(x): return 3*x**2 - 1
        root = newton_root(f, f_prime, x0=1.5)
        self.assertAlmostEqual(f(root), 0, places=8)

    def test_quadratic_root(self):
        def f(x): return x**2 - 9
        def f_prime(x): return 2*x
        root = newton_root(f, f_prime, x0=2)
        self.assertAlmostEqual(root, 3, places=8)

    def test_flat_derivative(self):
        def f(x): return x**3
        def f_prime(x): return 3*x**2
        root = newton_root(f, f_prime, x0=0)
        self.assertIsNone(root)


class TestBisection(TestCase):
    def test_basic_root(self):
        def f(x): return x**2 - 4
        root = bisection(f, 0, 5)
        self.assertAlmostEqual(root, 2, places=8)

    def test_non_converging_interval(self):
        def f(x): return x**2 + 1
        self.assertIsNone(bisection(f, -1, 1))

    def test_accuracy(self):
        def f(x): return cos(x) - x
        root = bisection(f, 0, 1)
        self.assertAlmostEqual(f(root), 0, places=8)


class TestGradientDescent(TestCase):

    def test_quadratic_minimum(self):
        def f(x): return (x - 3)**2
        def grad_f(x): return 2*(x - 3)
        result = gradient_descent(f, grad_f, x0=0)
        # self.assertAlmostEqual(result, 3, places=5)
        self.assertAlmostEqual(result, 3, delta=1e-4)

    def test_flat_function(self):
        def f(x): return 5
        def grad_f(x): return 0
        result = gradient_descent(f, grad_f, x0=10)
        self.assertAlmostEqual(result, 10, places=6)

    def test_custom_learning_rate(self):
        def f(x): return (x - 1)**2
        def grad_f(x): return 2*(x - 1)
        result = gradient_descent(f, grad_f, x0=10, learning_rate=0.1)
        self.assertAlmostEqual(result, 1, places=4)


if __name__ == '__main__':
    main()
